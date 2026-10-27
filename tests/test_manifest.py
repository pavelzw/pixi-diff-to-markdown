import io
import json
from pathlib import Path
from unittest import mock

import pytest
from typer.testing import CliRunner

from pixi_diff_to_markdown.cli import app
from pixi_diff_to_markdown.diff import generate_output
from pixi_diff_to_markdown.manifest import (
    load_manifest_universe,
    resolve_universes,
)
from pixi_diff_to_markdown.models import Diff
from pixi_diff_to_markdown.settings import MergeDependencies, Settings

REPO_ROOT = Path(__file__).resolve().parents[1]
ISSUE_79_JSON = REPO_ROOT / "tests/resources/diff-issue-79.json"

runner = CliRunner()

MANIFEST_TOML = """
[workspace]
platforms = ["linux-64", "osx-arm64", "osx-64", "win-64"]

[environments]
lint = []
py312 = []
"""

EXPECTED_LINT_CELL = "lint on {linux-64, osx-arm64, win-64}"


def write_manifest(tmp_path: Path) -> Path:
    manifest = tmp_path / "pixi.toml"
    manifest.write_text(MANIFEST_TOML)
    return manifest


def render_issue_79(manifest_path: Path | None = None) -> str:
    data = Diff.model_validate_json(ISSUE_79_JSON.read_text())
    settings = Settings.model_validate(
        {
            "merge-dependencies": MergeDependencies.yes,
            "explicit-column": True,
            **({"manifest-path": manifest_path} if manifest_path else {}),
        }
    )
    return generate_output(data.environment, settings)


def test_universe_from_toml(tmp_path: Path):
    universe = load_manifest_universe(write_manifest(tmp_path))
    assert universe.environments == frozenset({"default", "lint", "py312"})
    assert universe.platforms == frozenset(
        {"linux-64", "osx-arm64", "osx-64", "win-64"}
    )


def test_universe_from_lockfile():
    universe = load_manifest_universe(REPO_ROOT / "pixi.lock")
    assert {"default", "py315"} <= universe.environments
    assert "win-arm64" in universe.platforms


@pytest.mark.parametrize(
    "manifest_path_factory",
    [
        lambda tmp_path: write_manifest(tmp_path),
        lambda tmp_path: REPO_ROOT / "pixi.lock",
    ],
    ids=["from_toml", "from_lockfile"],
)
def test_issue_79_not_all_with_manifest(tmp_path: Path, manifest_path_factory):
    manifest_path = manifest_path_factory(tmp_path)
    output = render_issue_79(manifest_path)
    assert EXPECTED_LINT_CELL in output
    # the literal '*all*' label (whole universe covered) must be gone
    assert "|*all*|" not in output


def test_issue_79_default_anchor_without_manifest():
    """Even without a manifest, the implicit default env rules out *all*.

    Platforms stay inferred from the diff, so *all platforms* can still be
    printed; the environment label must become ``lint``.
    """
    output = render_issue_79(None)
    assert "lint on *all platforms*" in output
    assert "|*all*|" not in output


def test_full_universe_coverage_still_all(tmp_path: Path):
    """A package present in every declared env/platform is still labelled *all*."""
    diff = json.loads(ISSUE_79_JSON.read_text())
    lint_records = diff["environment"]["lint"]
    chosen_platforms = {
        platform: lint_records[platform] for platform in ("linux-64", "osx-arm64")
    }
    diff["environment"] = {
        "default": json.loads(json.dumps(chosen_platforms)),
        "lint": json.loads(json.dumps(chosen_platforms)),
    }
    diff_file = tmp_path / "diff.json"
    diff_file.write_text(json.dumps(diff))

    manifest = tmp_path / "pixi.toml"
    manifest.write_text(
        """
[workspace]
platforms = ["linux-64", "osx-arm64"]

[environments]
lint = []
"""
    )

    data = Diff.model_validate_json(diff_file.read_text())
    settings = Settings.model_validate(
        {
            "merge-dependencies": MergeDependencies.yes,
            "manifest-path": manifest,
        }
    )
    output = generate_output(data.environment, settings)
    assert "|*all*|" in output


def test_issue_79_cli_manifest_path(tmp_path: Path):
    manifest = write_manifest(tmp_path)
    with mock.patch(
        "pixi_diff_to_markdown.cli.stdin", io.StringIO(ISSUE_79_JSON.read_text())
    ):
        result = runner.invoke(
            app,
            [
                "--manifest-path",
                str(manifest),
                "--merge-dependencies",
                "yes",
                "--explicit-column",
            ],
        )
    assert result.exit_code == 0, result.stdout
    assert EXPECTED_LINT_CELL in result.stdout
    assert "|*all*|" not in result.stdout


def test_cli_rejects_missing_manifest(tmp_path: Path):
    missing = tmp_path / "does-not-exist.toml"
    with (
        mock.patch(
            "pixi_diff_to_markdown.cli.stdin",
            io.StringIO(ISSUE_79_JSON.read_text()),
        ),
        mock.patch("pixi_diff_to_markdown.cli.stderr", new=io.StringIO()),
    ):
        result = runner.invoke(app, ["--manifest-path", str(missing)])
    assert result.exit_code != 0


def test_missing_manifest_path_raises(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_manifest_universe(tmp_path / "missing" / "pixi.toml")


def test_universe_from_project_directory(tmp_path: Path):
    write_manifest(tmp_path)
    universe = load_manifest_universe(tmp_path)
    assert "lint" in universe.environments
    assert "osx-arm64" in universe.platforms


def test_universe_from_pyproject(tmp_path: Path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[project]
name = "example"

[tool.pixi.workspace]
platforms = ["linux-64", "osx-arm64"]

[tool.pixi.environments.lint]
"""
    )
    universe = load_manifest_universe(pyproject)
    assert universe.platforms == frozenset({"linux-64", "osx-arm64"})
    assert {"default", "lint"} <= universe.environments


def test_invalid_lockfile_raises_value_error(tmp_path: Path):
    (tmp_path / "pixi.toml").write_text("")
    (tmp_path / "pixi.lock").write_text(
        "version: 7\nenvironments:\n  default:\n    channels: []\n"
    )
    with pytest.raises(ValueError):
        load_manifest_universe(tmp_path / "pixi.toml")


def test_unsupported_manifest_file_raises(tmp_path: Path):
    unsupported = tmp_path / "pixi.cfg"
    unsupported.write_text("not a pixi manifest")
    with pytest.raises(ValueError, match="Unsupported manifest file"):
        load_manifest_universe(unsupported)


def test_resolve_unions_observed_and_declared(tmp_path: Path):
    manifest = write_manifest(tmp_path)
    environments, platforms = resolve_universes(
        {"new-feature"}, {"new-platform-99"}, manifest
    )
    assert {"default", "lint", "py312", "new-feature"} <= environments
    assert {"linux-64", "new-platform-99"} <= platforms
