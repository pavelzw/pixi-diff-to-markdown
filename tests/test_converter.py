import json

from pixi_diff_to_markdown.__main__ import generate_output
from pixi_diff_to_markdown.models import Environments

# CONFIGURATION: Configuration = {
#     "enable_change_type_column": True,
#     "enable_package_type_column": False,
#     "enable_explicit_type_column": False,
#     "split_tables": "no",
#     "hide_tables": False,
# }

def test_generate_table():
    with open("tests/resources/test.json") as f:
        data = json.load(f)
    data_parsed = Environments(data)
    actual_output = generate_output(data_parsed)
    with open("tests/resources/output.md") as f:
        expected_output = "".join(f.readlines())
    assert actual_output == expected_output