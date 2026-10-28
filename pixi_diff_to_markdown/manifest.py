"""Resolve the project-wide set of environments and platforms.

The ``pixi update --json`` diff only lists the environments and platforms for
which at least one package changed. Relying solely on that subset makes it
impossible to decide reliably whether an update covers ``*all*`` environments
or ``*all platforms*``. When the user points us at the project, we therefore
derive the project-wide universe from its ``pixi.lock`` (using ``py-rattler``)
or, when no lockfile is available, from its ``pixi.toml`` manifest.
"""

import tomllib
from dataclasses import dataclass
from pathlib import Path

from rattler.lock import LockFile


@dataclass(frozen=True)
class ManifestUniverse:
    """Environment and platform names declared by a pixi project."""

    environments: frozenset[str]
    platforms: frozenset[str]


def _resolve_paths(path: Path) -> tuple[Path | None, Path | None]:
    """Return the ``(manifest, lockfile)`` paths for a file, directory or lock.

    Either element can be ``None``: a lockfile-only input has no manifest, and a
    plain manifest has an optional sibling lock. A project directory without a
    ``pixi.toml`` falls back to ``pyproject.toml``.
    """
    if path.is_dir():
        manifest = path / "pixi.toml"
        if not manifest.is_file():
            pyproject = path / "pyproject.toml"
            manifest = pyproject if pyproject.is_file() else None
        return manifest, path / "pixi.lock"
    if path.suffix == ".toml":
        return path, path.parent / "pixi.lock"
    if path.suffix == ".lock" or path.name == "pixi.lock":
        return None, path
    raise ValueError(
        f"Unsupported manifest file '{path}'. Provide a pixi.toml, pixi.lock or its directory."
    )


def universe_from_lockfile(path: Path) -> ManifestUniverse:
    """Read the full environment/platform universe from a ``pixi.lock`` file."""
    lock = LockFile.from_path(path)
    lock_environments = list(lock.environments())
    environments = {name for name, _environment in lock_environments}
    platforms = {
        platform.name
        for _name, environment in lock_environments
        for platform in environment.platforms()
    }
    return ManifestUniverse(frozenset(environments), frozenset(platforms))


def universe_from_manifest(path: Path) -> ManifestUniverse:
    """Read platforms and named environments from a ``pixi.toml``/``pyproject.toml``."""
    data = tomllib.loads(path.read_text())
    workspace = data.get("workspace") or data.get("project") or {}
    platforms = set(workspace.get("platforms") or ())

    # Support the pixi integration inside a pyproject.toml as well.
    tool_pixi = data.get("tool", {}).get("pixi", {})
    if not platforms:
        tool_workspace = tool_pixi.get("workspace") or tool_pixi.get("project") or {}
        platforms = set(tool_workspace.get("platforms") or ())

    # The ``default`` environment always exists implicitly; ``[environments]``
    # declares the additional named environments.
    environments = {"default", *(data.get("environments") or {}).keys()}
    environments.update((tool_pixi.get("environments") or {}).keys())

    return ManifestUniverse(frozenset(environments), frozenset(platforms))


def load_manifest_universe(manifest_path: Path) -> ManifestUniverse:
    """Load the universe from the lockfile and/or the manifest next to it.

    When both a manifest (``pixi.toml``/``pyproject.toml``) and a ``pixi.lock``
    exist, their declarations are merged. Pixi allows a lockfile to be out of
    date with its manifest, e.g. when a new environment was added but not yet
    locked, so the manifest's platforms/environments are combined with the
    lockfile ones to keep the universe complete.
    """
    manifest_file, lock_file = _resolve_paths(manifest_path.expanduser())

    if (manifest_file is None or not manifest_file.is_file()) and (
        lock_file is None or not lock_file.is_file()
    ):
        raise FileNotFoundError(f"Could not find pixi manifest at '{manifest_path}'.")

    environments: set[str] = set()
    platforms: set[str] = set()
    if manifest_file is not None and manifest_file.is_file():
        declared = universe_from_manifest(manifest_file)
        environments |= declared.environments
        platforms |= declared.platforms
    if lock_file is not None and lock_file.is_file():
        try:
            locked = universe_from_lockfile(lock_file)
        except FileNotFoundError, ValueError:
            raise
        except Exception as e:  # py-rattler raises its own parse error type
            raise ValueError(f"Could not parse pixi lockfile '{lock_file}': {e}") from e
        environments |= locked.environments
        platforms |= locked.platforms

    return ManifestUniverse(frozenset(environments), frozenset(platforms))


def resolve_universes(
    observed_environments: set[str],
    observed_platforms: set[str],
    manifest_path: Path | None,
) -> tuple[set[str], set[str]]:
    """Determine the universe used to decide the ``*all*`` labels.

    Both returned sets always include every observed environment and platform so
    an update for an axis that a slightly outdated manifest/lockfile does not yet
    know about is still represented (and never triggers a ``KeyError``).

    Without a manifest, the sets are derived from the diff itself, except that
    every pixi workspace implicitly defines a ``default`` environment. If
    ``default`` is absent from the diff, the update is guaranteed not to cover
    all environments, so it is added to the inferred universe.
    """
    if manifest_path is not None:
        universe = load_manifest_universe(manifest_path)
        return (
            set(universe.environments) | observed_environments,
            set(universe.platforms) | observed_platforms,
        )

    environments = set(observed_environments)
    if environments and "default" not in environments:
        environments.add("default")
    return environments, set(observed_platforms)
