from itertools import zip_longest
from typing import Literal

import pydantic
from ordered_enum import OrderedEnum
from pydantic import ConfigDict, field_validator
from rattler import Version


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

    model_config = ConfigDict(frozen=True)


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
        return change_type_self < change_type_other

    def __gt__(self, other):
        if self.explicit != other.explicit:
            return self.explicit > other.explicit
        change_type_self = calculate_change_type(self)
        change_type_other = calculate_change_type(other)
        return change_type_self > change_type_other


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
