import io
from unittest import mock

import pytest
from typer.testing import CliRunner

from pixi_diff_to_markdown.cli import app

runner = CliRunner()


@pytest.mark.parametrize(
    ("stdin_content", "expected_error_fragment"),
    [
        ("not valid json", "Invalid JSON"),
        ("", "Invalid JSON"),
        ('{"foo": "bar"}', "environment\n  Field required"),
    ],
    ids=["invalid_json", "empty_input", "wrong_schema"],
)
def test_invalid_input(stdin_content: str, expected_error_fragment: str):
    stderr_capture = io.StringIO()
    with (
        mock.patch("pixi_diff_to_markdown.cli.stdin", io.StringIO(stdin_content)),
        mock.patch("pixi_diff_to_markdown.cli.stderr", stderr_capture),
    ):
        result = runner.invoke(app)
    assert result.exit_code != 0
    stderr_output = stderr_capture.getvalue()
    assert "Error: Invalid input" in stderr_output
    assert expected_error_fragment in stderr_output
