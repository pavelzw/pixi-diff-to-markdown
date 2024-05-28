from itertools import zip_longest
from typing import Literal

import pydantic
from ordered_enum import OrderedEnum
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


class CondaVersion(pydantic.BaseModel):
    version: str
    build: str


class PyPiVersion(pydantic.BaseModel):
    version: str


def calculate_change_type(update_spec: "UpdateSpec") -> ChangeType:
    if update_spec.before is None:
        assert update_spec.after is not None
        return ChangeType.ADDED
    if update_spec.after is None:
        assert update_spec.before is not None
        return ChangeType.REMOVED
    old_version = Version(update_spec.before.version)
    new_version = Version(update_spec.after.version)
    if old_version == new_version:
        assert type(update_spec.before) == CondaVersion
        assert type(update_spec.after) == CondaVersion
        assert update_spec.before.build != update_spec.after.build
        return ChangeType.BUILD

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
    before: CondaVersion | PyPiVersion | None = None
    after: CondaVersion | PyPiVersion | None = None
    type: Literal["conda", "pypi"]
    # if not set, defaults to default
    explicit: bool = False

    def __lt__(self, other):
        change_type_self = calculate_change_type(self)
        change_type_other = calculate_change_type(other)
        return change_type_self < change_type_other

    def __gt__(self, other):
        change_type_self = calculate_change_type(self)
        change_type_other = calculate_change_type(other)
        return change_type_self > change_type_other


class Dependencies(pydantic.RootModel):
    root: list[UpdateSpec]


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]
