from enum import Enum
from typing import Literal, TypedDict

import pydantic


class Configuration(TypedDict):
    enable_change_type_column: bool
    # False implies cursive dependency names
    enable_explicit_type_column: bool
    enable_package_type_column: bool
    split_tables: Literal["no", "environment", "platform"]
    hide_tables: bool


class ChangeType(Enum):
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


class DependencyType(Enum):
    EXPLICIT = "Explicit"
    IMPLICIT = "Implicit"


class CondaVersion(pydantic.BaseModel):
    version: str
    build: str


class UpdateSpec(pydantic.BaseModel):
    before: CondaVersion
    after: CondaVersion
    type_: Literal["conda"]
    explicit: bool


class Dependencies(pydantic.RootModel):
    root: dict[str, UpdateSpec]


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]
