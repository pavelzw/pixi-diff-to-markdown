import json

import pytest

from pixi_diff_to_markdown.diff import generate_output
from pixi_diff_to_markdown.models import Environments
from pixi_diff_to_markdown.settings import Settings, SplitTables


@pytest.mark.parametrize("change_type_column", [True, False])
@pytest.mark.parametrize("package_type_column", [True, False])
@pytest.mark.parametrize("explicit_column", [True, False])
@pytest.mark.parametrize("split_tables", ["no", "environment", "platform"])
@pytest.mark.parametrize("hide_tables", [True, False])
def test_generate_table(
    change_type_column: bool,
    package_type_column: bool,
    explicit_column: bool,
    split_tables: SplitTables,
    hide_tables: bool,
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
    with open("tests/resources/test.json") as f:
        data = json.load(f)
    data_parsed = Environments(data)
    actual_output = generate_output(data_parsed, settings)
    file_name = f"tests/resources/output/split-tables-{settings.split_tables.value}_hide-tables-{settings.hide_tables}_change-type-{settings.change_type_column}_explicit-{settings.explicit_column}_package-type-{settings.package_type_column}.md"
    with open(file_name) as f:
        expected_output = "".join(f.readlines())
    assert actual_output == expected_output
    # with open(file_name, "w") as f:
    #     f.writelines(actual_output)
