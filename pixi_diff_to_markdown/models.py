from typing import Literal, TypedDict

import pydantic


class Configuration(TypedDict):
    enable_change_column: bool
    # False implies cursive dependency names
    enable_explicit_implicit_column: bool
    enable_package_type_column: bool
    split_tables: Literal["no", "environment", "platform"]
    hide_tables: bool


class CondaVersion(pydantic.BaseModel):
    version: str
    build: str


class UpdateSpec(pydantic.BaseModel):
    before: CondaVersion
    after: CondaVersion
    type_: Literal["conda"]


class Dependencies(pydantic.RootModel):
    root: dict[str, UpdateSpec]


class Platforms(pydantic.RootModel):
    root: dict[str, Dependencies]


class Environments(pydantic.RootModel):
    root: dict[str, Platforms]
