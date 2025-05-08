from dataclasses import dataclass
from enum import Enum
from itertools import zip_longest
from typing import Any, Self

import pydantic
from ordered_enum import OrderedEnum
from pydantic import ConfigDict, computed_field, field_validator, model_validator
from rattler import Version

from pixi_diff_to_markdown.markdown import (
    generate_markdown_table_header,
    generate_table_line,
)
from pixi_diff_to_markdown.settings import Settings

UpdatedEnvironments = list[tuple[str, str]]


class ChangeType(OrderedEnum):
    ADDED = "Added"
    REMOVED = "Removed"
    MAJOR_UP = "Major Upgrade"
    MAJOR_DOWN = "Major Downgrade"
    MINOR_UP = "Minor Upgrade"
    MINOR_DOWN = "Minor Downgrade"
    PATCH_UP = "Patch Upgrade"
    PATCH_DOWN = "Patch Downgrade"
    OTHER = "Other"
    BUILD = "Only build string"


class DependencyType(OrderedEnum):
    EXPLICIT = "Explicit"
    IMPLICIT = "Implicit"


class PackageType(Enum):
    CONDA = "conda"
    PYPI = "pypi"

    def __str__(self):
        return self.value


class PackageInformation(pydantic.BaseModel):
    conda: str | None = None
    pypi: str | None = None
    # called version in the lockfile, only used for pypi packages
    pypi_version: str | None = None

    @model_validator(mode="before")
    @classmethod
    def transform_before(cls, data: Any) -> Any:
        # backwards compatibility for lockfile <v6 (pixi <0.39.0)
        # before v6, the build and version were stored explicitly in the lockfile
        # after v6, the build and version are stored implicitly in the conda url
        assert isinstance(data, dict)
        if "conda" not in data and "pypi" not in data:
            # this maps all old lockfiles to conda packages, not pretty but should be fine
            build = data.get("build", "placeholder_0")
            assert isinstance(build, str)
            version = data.get("version", "0.0.0")
            assert isinstance(version, str)
            data["conda"] = (
                f"https://url/to/channel/subdir/placeholder-{version}-{build}.conda"
            )

        if "pypi" in data:
            if data["pypi"].startswith("git+https://"):
                # in case of a git dependency, we don't have a version
                data["version"] = None
            assert "version" in data
            data["pypi_version"] = data["version"]
        return data

    @model_validator(mode="after")
    def validate_after(self) -> Self:
        assert self.conda is not None or self.pypi is not None
        if self.pypi is None:
            assert self.pypi_version is None
        return self

    def _conda_package_name(self) -> str:
        assert self.conda is not None
        return self.conda.split("/")[-1].removesuffix(".tar.bz2").removesuffix(".conda")

    @computed_field
    @property
    def build(self) -> str | None:
        if self.conda is None:
            return None
        return self._conda_package_name().split("-")[-1]

    @computed_field
    @property
    def version(self) -> str:
        if self.conda is None:
            # pypi_version can be none for git dependencies
            return self.pypi_version or "none"
        return self._conda_package_name().split("-")[-2]


class UpdateSpec(pydantic.BaseModel):
    name: str
    before: PackageInformation | None = None
    after: PackageInformation | None = None
    type: PackageType
    # if not set, defaults to implicit
    explicit: DependencyType = DependencyType.IMPLICIT

    model_config = ConfigDict(frozen=True)

    def __eq__(self, other):
        return isinstance(other, UpdateSpec) and hash(self) == hash(other)

    def __hash__(self):
        """
        Two elements where the versions are the same but the hashes aren't should be considered the same.
        Thus, don't include before and after in the hash but only `self.change_type` and `self.before_after_str`.
        """
        return hash(
            (
                self.name,
                self.explicit,
                self.type,
                self.change_type,
                *self.before_after_str(),
            )
        )

    @field_validator("explicit", mode="before")
    @classmethod
    def transform(cls, explicit: bool) -> DependencyType:
        return DependencyType.EXPLICIT if explicit else DependencyType.IMPLICIT

    def __lt__(self, other):
        if not isinstance(other, UpdateSpec):
            return NotImplemented
        if self.explicit != other.explicit:
            return self.explicit < other.explicit
        change_type_self = self.change_type
        change_type_other = other.change_type
        if change_type_self != change_type_other:
            return change_type_self < change_type_other
        return self.name < other.name

    @computed_field
    @property
    def change_type(self) -> ChangeType:
        if self.before is None:
            assert self.after is not None
            return ChangeType.ADDED
        if self.after is None:
            assert self.before is not None
            return ChangeType.REMOVED
        if self.before.version == self.after.version:
            if self.before.build == self.after.build:
                # this can happen when only the URL to the package changes
                return ChangeType.OTHER
            return ChangeType.BUILD

        old_version = Version(self.before.version)
        new_version = Version(self.after.version)

        padded_vers = zip_longest(
            old_version.segments(), new_version.segments(), fillvalue=[0]
        )
        for idx_vers_element_differs, vers_element in enumerate(padded_vers):
            if vers_element[0] != vers_element[1]:
                break
        else:
            assert False, "padded_vars is not empty"
        if old_version > new_version:
            if idx_vers_element_differs == 0:
                return ChangeType.MAJOR_DOWN
            elif idx_vers_element_differs == 1:
                return ChangeType.MINOR_DOWN
            elif idx_vers_element_differs == 2:
                return ChangeType.PATCH_DOWN
            else:
                return ChangeType.OTHER
        else:
            if idx_vers_element_differs == 0:
                return ChangeType.MAJOR_UP
            elif idx_vers_element_differs == 1:
                return ChangeType.MINOR_UP
            elif idx_vers_element_differs == 2:
                return ChangeType.PATCH_UP
            else:
                return ChangeType.OTHER

    def before_after_str(self) -> tuple[str, str]:
        change_type = self.change_type
        before: str | None
        after: str | None
        if change_type == ChangeType.ADDED:
            before = ""
            after = self.after.version
        elif change_type == ChangeType.REMOVED:
            before = self.before.version
            after = ""
        elif change_type == ChangeType.BUILD:
            before = self.before.build
            after = self.after.build
        else:
            before = self.before.version
            after = self.after.version
        assert before is not None
        assert after is not None
        return before, after


@dataclass
class TableRow:
    update_spec: UpdateSpec
    # used when the environment / platform column is shown, i.e. when the tables are split by environment
    platform: str | None = None
    # used when the environment / platform column is shown, i.e. when the tables are not split
    environment_platform: str | None = None
    # the updated environments that this update spec applies to
    # if None, it only applies to one environment (the tables are not merged)
    updated_environments: str | None = None

    def __lt__(self, other):
        if not isinstance(other, TableRow):
            return NotImplemented
        return self.update_spec < other.update_spec

    def generate_table_line(self, settings: Settings) -> str:
        change_type = self.update_spec.change_type
        before, after = self.update_spec.before_after_str()

        if (
            change_type == ChangeType.MAJOR_DOWN
            or change_type == ChangeType.MINOR_DOWN
            or change_type == ChangeType.PATCH_DOWN
        ):
            maybe_downgrade_ref = "[^2]"
        else:
            maybe_downgrade_ref = ""
        columns = []
        if self.platform is not None:
            columns.append(self.platform)
        if self.environment_platform is not None:
            columns.append(self.environment_platform)
        if (
            not settings.explicit_column
            and self.update_spec.explicit == DependencyType.EXPLICIT
        ):
            package_name_formatted = f"**{self.update_spec.name}**"
        else:
            package_name_formatted = self.update_spec.name
        if settings.create_links_for_packages and self.update_spec.after is not None:
            if self.update_spec.after.conda is not None:
                after_url = self.update_spec.after.conda
                for public_channel in [
                    "conda-forge",
                    "bioconda",
                    "nvidia",
                    "rapidsai",
                    "robostack",
                    "robostack-humble",
                    "robostack-staging",
                ]:
                    if after_url.startswith(
                        f"https://conda.anaconda.org/{public_channel}"
                    ):
                        package_name_formatted = f"[{package_name_formatted}](https://prefix.dev/channels/{public_channel}/packages/{self.update_spec.name})"
                        break
                if (
                    after_url.startswith("https://prefix.dev/")
                    or after_url.startswith("https://repo.prefix.dev/")
                    or after_url.startswith("https://fast.prefix.dev/")
                ):
                    channel_name = after_url.split("/")[3]
                    package_name_formatted = f"[{package_name_formatted}](https://prefix.dev/channels/{channel_name}/packages/{self.update_spec.name})"
            else:
                assert self.update_spec.after.pypi is not None
                after_url = self.update_spec.after.pypi
                assert after_url is not None
                if after_url.startswith("https://files.pythonhosted.org/packages"):
                    package_name_formatted = f"[{package_name_formatted}](https://pypi.org/project/{self.update_spec.name})"
        columns.extend(
            [
                package_name_formatted + maybe_downgrade_ref,
                before,
                after,
            ]
        )
        if settings.change_type_column:
            columns.append(change_type.value)
        if settings.explicit_column:
            columns.append(
                str(self.update_spec.explicit == DependencyType.EXPLICIT).lower()
            )
        if settings.package_type_column:
            columns.append(str(self.update_spec.type))
        if self.updated_environments is not None:
            columns.append(self.updated_environments)
        return generate_table_line(*columns)


@dataclass
class DependencyTable:
    rows: list[TableRow]
    use_updated_environment_column: bool = False

    def generate_header(self, settings: Settings) -> str:
        columns = []
        columns.extend(
            [
                f"Dependency{'[^1]' if not settings.explicit_column else ''}",
                "Before",
                "After",
            ]
        )
        if settings.change_type_column:
            columns.append("Change")
        if settings.explicit_column:
            columns.append("Explicit")
        if settings.package_type_column:
            columns.append("Package")
        if self.use_updated_environment_column:
            columns.append("Environments")
        return generate_markdown_table_header(columns)

    def to_string(self, settings: Settings) -> str:
        header = self.generate_header(settings)
        return (
            header
            + "\n"
            + "\n".join([row.generate_table_line(settings) for row in self.rows])
        )


class Dependencies(pydantic.RootModel):
    root: list[UpdateSpec]

    def __len__(self):
        return len(self.root)

    def to_table(self) -> DependencyTable:
        rows: list[TableRow] = []
        for update_spec in self.root:
            table_row = TableRow(update_spec=update_spec)
            rows.append(table_row)
        return DependencyTable(sorted(rows))


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]


class Diff(pydantic.BaseModel):
    environment: Environments
    version: int
