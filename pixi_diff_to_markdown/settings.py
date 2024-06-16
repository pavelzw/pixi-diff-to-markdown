from enum import Enum

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

from pixi_diff_to_markdown.pydantic_settings_extension import (
    TomlWithTableHeaderConfigSettingsSource,
)


class MergeDependencies(str, Enum):
    no = "no"
    merge_all = "merge-all"
    split_explicit = "split-explicit"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # pixi.toml has higher priority if it exists
        toml_file=["pyproject.toml", "pixi.toml"],
        env_prefix="PIXI_DIFF_TO_MARKDOWN_",
        alias_generator=lambda x: x.replace("_", "-"),
    )
    change_type_column: bool = True
    package_type_column: bool = True
    explicit_column: bool = False
    merge_dependencies: MergeDependencies = MergeDependencies.split_explicit
    hide_tables: bool = False

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,  # correspond to CLI arguments
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            TomlWithTableHeaderConfigSettingsSource(settings_cls),
        )
