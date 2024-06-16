from pathlib import Path

import pytest

from pixi_diff_to_markdown.diff import generate_output
from pixi_diff_to_markdown.models import (
    Diff,
)
from pixi_diff_to_markdown.settings import Settings, SplitTables


@pytest.mark.parametrize(
    "diff_file",
    ["diff-example.json", "diff-polarify.json", "diff-pixi-diff-to-markdown.json"],
)
@pytest.mark.parametrize("change_type_column", [True, False])
@pytest.mark.parametrize("package_type_column", [True, False])
@pytest.mark.parametrize("explicit_column", [True, False])
@pytest.mark.parametrize("split_tables", SplitTables.__members__.values())
@pytest.mark.parametrize("hide_tables", [True, False])
def test_generate_table(
    diff_file: str,
    change_type_column: bool,
    package_type_column: bool,
    explicit_column: bool,
    split_tables: SplitTables,
    hide_tables: bool,
    write_results: bool,
):
    settings = Settings.model_validate(
        {
            "change-type-column": change_type_column,
            "package-type-column": package_type_column,
            "explicit-column": explicit_column,
            "split-tables": split_tables,
            "hide-tables": hide_tables,
        }
    )
    diff_path = Path(f"tests/resources/{diff_file}")
    data_parsed = Diff.model_validate_json(diff_path.read_text())
    actual_output = generate_output(data_parsed.environment, settings)
    file_name = f"tests/resources/{diff_file.split(".")[0]}/split-tables-{settings.split_tables.value}_hide-tables-{settings.hide_tables}_change-type-{settings.change_type_column}_explicit-{settings.explicit_column}_package-type-{settings.package_type_column}.md"
    if write_results:
        with open(file_name, "w") as f:
            f.writelines(actual_output)
    else:
        with open(file_name) as f:
            expected_output = "".join(f.readlines())
        assert actual_output == expected_output


def test_setting_selection():
    assert True
    # TODO: ensure best settings are selected by default
