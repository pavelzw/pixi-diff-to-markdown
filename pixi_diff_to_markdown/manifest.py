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


def _lockfile_path(path: Path) -> Path:
    """Return the ``pixi.lock`` path for a manifest, lockfile or directory.

    An explicit lockfile is returned as-is; anything else resolves to the
    ``pixi.lock`` sibling (next to a manifest) or child (inside a directory).
    """
    if path.suffix == ".lock" or path.name == "pixi.lock":
        return path
    return path.parent / "pixi.lock" if path.is_file() else path / "pixi.lock"


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
    """Load the universe from a lockfile if present, otherwise from the manifest."""
    path = manifest_path.expanduser()
    lockfile = _lockfile_path(path)
    if lockfile.is_file():
        try:
            return universe_from_lockfile(lockfile)
        except FileNotFoundError, ValueError:
            raise
        except Exception as e:  # py-rattler raises its own parse error type
            raise ValueError(f"Could not parse pixi lockfile '{lockfile}': {e}") from e

    if not path.exists():
        raise FileNotFoundError(f"Could not find pixi manifest at '{manifest_path}'.")
    if path.is_dir():
        path = path / "pixi.toml"
    if path.suffix != ".toml":
        raise ValueError(
            f"Unsupported manifest file '{path}'. Provide a pixi.toml, pixi.lock or its directory."
        )
    return universe_from_manifest(path)


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
