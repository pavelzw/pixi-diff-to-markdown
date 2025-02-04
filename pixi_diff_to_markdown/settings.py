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
    yes = "yes"
    split_explicit = "split-explicit"


class HideTables(str, Enum):
    no = "no"
    yes = "yes"
    auto = "auto"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # pixi.toml has higher priority if it exists
        toml_file=["pyproject.toml", "pixi.toml"],
        env_prefix="PIXI_DIFF_TO_MARKDOWN_",
        alias_generator=lambda x: x.replace("_", "-"),
    )
    change_type_column: bool = True
    package_type_column: bool = False
    explicit_column: bool = False
    merge_dependencies: MergeDependencies
    hide_tables: HideTables = HideTables.auto
    max_expanded_rows: int = 10
    create_links_for_packages: bool = True

    def __init__(
        self, inferred_merge_dependencies: MergeDependencies | None = None, **data
    ):
        if "merge-dependencies" not in data and inferred_merge_dependencies is not None:
            data["merge-dependencies"] = inferred_merge_dependencies
        super().__init__(**data)

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
