from pathlib import Path

import pytest

from pixi_diff_to_markdown.diff import generate_output
from pixi_diff_to_markdown.models import (
    Diff,
)
from pixi_diff_to_markdown.settings import HideTables, MergeDependencies, Settings


@pytest.mark.parametrize(
    "diff_file",
    [
        "diff-example-v6-lockfile.json",
        "diff-example.json",
        "diff-polarify.json",
        "diff-pixi-diff-to-markdown.json",
    ],
)
@pytest.mark.parametrize("change_type_column", [True, False])
@pytest.mark.parametrize("package_type_column", [True, False])
@pytest.mark.parametrize("explicit_column", [True, False])
@pytest.mark.parametrize("merge_dependencies", MergeDependencies.__members__.values())
@pytest.mark.parametrize("hide_tables", [HideTables.no, HideTables.yes])
def test_generate_table(
    diff_file: str,
    change_type_column: bool,
    package_type_column: bool,
    explicit_column: bool,
    merge_dependencies: MergeDependencies,
    hide_tables: HideTables,
    write_results: bool,
):
    settings = Settings.model_validate(
        {
            "change-type-column": change_type_column,
            "package-type-column": package_type_column,
            "explicit-column": explicit_column,
            "merge-dependencies": merge_dependencies,
            "hide-tables": hide_tables,
        }
    )
    diff_path = Path(f"tests/resources/{diff_file}")
    data_parsed = Diff.model_validate_json(diff_path.read_text())
    actual_output = generate_output(data_parsed.environment, settings)
    file_name = f"tests/resources/{diff_file.split('.')[0]}/merge-{settings.merge_dependencies.value}_hide-{settings.hide_tables.value}_change-type-{settings.change_type_column}_explicit-{settings.explicit_column}_package-type-{settings.package_type_column}.md"
    if write_results:
        with open(file_name, "w") as f:
            f.writelines(actual_output)
    else:
        with open(file_name) as f:
            expected_output = "".join(f.readlines())
        assert actual_output == expected_output


@pytest.mark.parametrize("change_type_column", [False])
@pytest.mark.parametrize("package_type_column", [False])
@pytest.mark.parametrize("explicit_column", [True])
@pytest.mark.parametrize("merge_dependencies", [MergeDependencies.split_explicit])
@pytest.mark.parametrize("hide_tables", [HideTables.no])
def test_empty_update(
    change_type_column: bool,
    package_type_column: bool,
    explicit_column: bool,
    merge_dependencies: MergeDependencies,
    hide_tables: bool,
):
    settings = settings = Settings.model_validate(
        {
            "change-type-column": change_type_column,
            "package-type-column": package_type_column,
            "explicit-column": explicit_column,
            "merge-dependencies": merge_dependencies,
            "hide-tables": hide_tables,
        }
    )
    data_parsed = Diff.model_validate_json(r'{"version": 1, "environment": {}}')
    actual_output = generate_output(data_parsed.environment, settings)
    assert actual_output == ""
