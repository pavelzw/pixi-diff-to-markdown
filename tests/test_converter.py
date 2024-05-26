import json

import pytest

from pixi_diff_to_markdown.__main__ import generate_output
from pixi_diff_to_markdown.models import Configuration, Environments


@pytest.mark.parametrize("enable_change_type_column", [True, False])
@pytest.mark.parametrize("enable_package_type_column", [True, False])
@pytest.mark.parametrize("enable_explicit_type_column", [True, False])
@pytest.mark.parametrize("split_tables", ["no", "environment", "platform"])
@pytest.mark.parametrize("hide_tables", [True, False])
def test_generate_table(
    enable_change_type_column,
    enable_package_type_column,
    enable_explicit_type_column,
    split_tables,
    hide_tables,
):
    configuration: Configuration = {
        "enable_change_type_column": enable_change_type_column,
        "enable_package_type_column": enable_package_type_column,
        "enable_explicit_type_column": enable_explicit_type_column,
        "split_tables": split_tables,
        "hide_tables": hide_tables,
    }
    with open("tests/resources/test.json") as f:
        data = json.load(f)
    data_parsed = Environments(data)
    actual_output = generate_output(data_parsed, configuration)
    file_name = f"tests/resources/output/split-tables-{split_tables}_hide-tables-{hide_tables}_change-type-{enable_change_type_column}_explicit-type-{enable_explicit_type_column}_package-type-{enable_package_type_column}.md"
    with open(file_name) as f:
        expected_output = "".join(f.readlines())
    assert actual_output == expected_output
    # with open(file_name, "w") as f:
    #     f.writelines(actual_output)
