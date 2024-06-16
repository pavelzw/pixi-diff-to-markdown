from itertools import zip_longest
from typing import Literal, Self

import pydantic
from ordered_enum import OrderedEnum
from pydantic import ConfigDict, field_validator, model_validator
from rattler import Version

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


def calculate_change_type(update_spec: "UpdateSpec") -> ChangeType:
    if update_spec.before is None:
        assert update_spec.after is not None
        return ChangeType.ADDED
    if update_spec.after is None:
        assert update_spec.before is not None
        return ChangeType.REMOVED
    if update_spec.before.version is None:
        assert update_spec.after.version is None
        assert update_spec.before.build is not None
        assert update_spec.after.build is not None
        return ChangeType.BUILD

    assert update_spec.after.version is not None
    assert update_spec.before.version != update_spec.after.version
    old_version = Version(update_spec.before.version)
    new_version = Version(update_spec.after.version)

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


class UpdateSpec(pydantic.BaseModel):
    name: str
    before: PackageInformation | None = None
    after: PackageInformation | None = None
    type: Literal["conda", "pypi"]
    # if not set, defaults to implicit
    explicit: DependencyType = DependencyType.IMPLICIT

    model_config = ConfigDict(frozen=True)

    @field_validator("explicit", mode="before")
    @classmethod
    def transform(cls, explicit: bool) -> DependencyType:
        return DependencyType.EXPLICIT if explicit else DependencyType.IMPLICIT

    def __lt__(self, other):
        if self.explicit != other.explicit:
            return self.explicit < other.explicit
        change_type_self = calculate_change_type(self)
        change_type_other = calculate_change_type(other)
        if change_type_self != change_type_other:
            return change_type_self < change_type_other
        return self.name < other.name

    def __gt__(self, other):
        if self.explicit != other.explicit:
            return self.explicit > other.explicit
        change_type_self = calculate_change_type(self)
        change_type_other = calculate_change_type(other)
        if change_type_self != change_type_other:
            return change_type_self > change_type_other
        return self.name > other.name


class Dependencies(pydantic.RootModel):
    root: list[UpdateSpec]


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]


class Diff(pydantic.BaseModel):
    environment: Environments
    version: int


class EnvironmentOrPlatform(pydantic.RootModel):
    root: str | tuple[str, str]
