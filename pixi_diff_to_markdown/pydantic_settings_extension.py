from pathlib import Path

from pydantic_settings import TomlConfigSettingsSource, BaseSettings
from pydantic_settings.sources import PathType, DEFAULT_PATH

class TomlWithTableHeaderConfigSettingsSource(TomlConfigSettingsSource):
    """
    A source class that loads variables from a TOML file but only inside a header.
    """

    def __init__(
        self,
        settings_cls: type[BaseSettings],
        toml_file: PathType | None = DEFAULT_PATH,
    ) -> None:
        self.toml_file_path = toml_file if toml_file != DEFAULT_PATH else settings_cls.model_config.get('toml_file')
        self.toml_table_header: tuple[str, ...] = settings_cls.model_config.get(
            'pyproject_toml_table_header', ('tool', 'pydantic-settings')
        )
        self.toml_data = self._read_files(self.toml_file_path)
        for key in self.toml_table_header:
            self.toml_data = self.toml_data.get(key, {})
        super(TomlConfigSettingsSource, self).__init__(settings_cls, self.toml_data)
