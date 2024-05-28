from typing import Type
from pathlib import Path

from pydantic import Field, AliasGenerator, AliasChoices
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, TomlConfigSettingsSource

from pixi_diff_to_markdown.pydantic_settings_extension import TomlWithTableHeaderConfigSettingsSource


from enum import Enum
class SplitTables(str, Enum):
    no = "no"
    environment = "environment"
    platform = "platform"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # pixi.toml has higher priority if it exists
        toml_file=['pyproject.toml', 'pixi.toml'],
        env_prefix='PIXI_DIFF_TO_MARKDOWN_',
        pyproject_toml_table_header=("tool", "pixi-diff-to-markdown"),
        alias_generator=lambda x: x.replace("_", "-"),
    )
    change_type_column: bool = True
    package_type_column: bool = True
    explicit_column: bool = False
    split_tables: SplitTables = "platform"
    hide_tables: bool = False


    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource, # correspond to CLI arguments
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return init_settings, env_settings, TomlWithTableHeaderConfigSettingsSource(settings_cls)
