from dataclasses import dataclass
from enum import Enum
from itertools import zip_longest
from typing import Literal, Self

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
    version: str | None = None
    build: str | None = None

    def __hash__(self):
        return hash((self.version, self.build))

    # two elements where the versions are the same but the hashes aren't should be considered the same
    # thus, only include the build string if the version is not set (i.e. no version update)
    @model_validator(mode="after")
    def transform(self) -> Self:
        if self.version is not None:
            self.build = None
        return self


class UpdateSpec(pydantic.BaseModel):
    name: str
    before: PackageInformation | None = None
    after: PackageInformation | None = None
    type: PackageType
    # if not set, defaults to implicit
    explicit: DependencyType = DependencyType.IMPLICIT

    model_config = ConfigDict(frozen=True)

    @field_validator("explicit", mode="before")
    @classmethod
    def transform(cls, explicit: bool) -> DependencyType:
        return DependencyType.EXPLICIT if explicit else DependencyType.IMPLICIT

    def __lt__(self, other):
        if not isinstance(other, UpdateSpec):
            return NotImplemented
        if self.explicit != other.explicit:
            return self.explicit < other.explicit
        change_type_self: ChangeType = self.change_type  # type: ignore[assignment]
        change_type_other: ChangeType = other.change_type  # type: ignore[assignment]
        if change_type_self != change_type_other:
            return change_type_self < change_type_other
        return self.name < other.name

    @computed_field
    def change_type(self) -> ChangeType:
        if self.before is None:
            assert self.after is not None
            return ChangeType.ADDED
        if self.after is None:
            assert self.before is not None
            return ChangeType.REMOVED
        if self.before.version is None:
            assert self.after.version is None
            assert self.before.build is not None
            assert self.after.build is not None
            return ChangeType.BUILD

        assert self.after.version is not None
        assert self.before.version != self.after.version
        old_version = Version(self.before.version)
        new_version = Version(self.after.version)

        padded_vers = zip_longest(
            old_version.segments(), new_version.segments(), fillvalue=[0]
        )
        for idx_vers_element_differs, vers_element in enumerate(padded_vers):
            if vers_element[0] != vers_element[1]:
                break
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
        change_type: ChangeType = self.change_type  # type: ignore[assignment]
        before: str | None
        after: str | None
        if change_type == ChangeType.ADDED:
            before = ""
            after = self.after.version  # type: ignore[union-attr]
        elif change_type == ChangeType.REMOVED:
            before = self.before.version  # type: ignore[union-attr]
            after = ""
        elif change_type == ChangeType.BUILD:
            before = self.before.build  # type: ignore[union-attr]
            after = self.after.build  # type: ignore[union-attr]
        else:
            before = self.before.version  # type: ignore[union-attr]
            after = self.after.version  # type: ignore[union-attr]
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
        # TODO: fix mypy issue
        change_type: ChangeType = self.update_spec.change_type  # type: ignore[assignment]
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
    use_platform_column: bool = False
    use_environment_platform_column: bool = False
    use_updated_environment_column: bool = False

    def generate_header(self, settings: Settings) -> str:
        columns = []
        orientations: list[Literal["left", "right", "center"]] = []
        if self.use_platform_column:
            columns.append("Platform")
            orientations.append("right")
        if self.use_environment_platform_column:
            columns.append("Environment / Platform")
            orientations.append("right")
        columns.extend(["Dependency", "Before", "After"])
        orientations.extend(["left", "left", "left"])
        if settings.change_type_column:
            columns.append("Change")
            orientations.append("left")
        if settings.explicit_column:
            columns.append("Explicit")
            orientations.append("left")
        if settings.package_type_column:
            columns.append("Package")
            orientations.append("left")
        if self.use_updated_environment_column:
            columns.append("Environments")
            orientations.append("left")
        return generate_markdown_table_header(columns, orientations)

    def to_string(self, settings: Settings) -> str:
        header = self.generate_header(settings)
        return (
            header
            + "\n"
            + "\n".join([row.generate_table_line(settings) for row in self.rows])
        )


class Dependencies(pydantic.RootModel):
    root: list[UpdateSpec]

    def to_table(self, settings: Settings) -> DependencyTable:
        rows: list[TableRow] = []
        for update_spec in self.root:
            table_row = TableRow(update_spec=update_spec)
            rows.append(table_row)
        return DependencyTable(sorted(rows))


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]

    def to_table(self, settings: Settings) -> DependencyTable:
        rows = []
        for platform, dependencies in self.root.items():
            for i, (update_spec) in enumerate(sorted(dependencies.root)):
                table_row = TableRow(
                    update_spec=update_spec,
                    platform=platform if i == 0 else "",
                )
                rows.append(table_row)
        return DependencyTable(rows, use_platform_column=True)


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]

    def to_table(self, settings: Settings) -> DependencyTable:
        rows = []
        for environment, platforms in self.root.items():
            for platform, dependencies in platforms.root.items():
                for i, update_spec in enumerate(sorted(dependencies.root)):
                    table_row = TableRow(
                        update_spec=update_spec,
                        environment_platform=f"{environment} / {platform}"
                        if i == 0
                        else "",
                    )
                    rows.append(table_row)
        return DependencyTable(rows, use_environment_platform_column=True)


class Diff(pydantic.BaseModel):
    environment: Environments
    version: int
