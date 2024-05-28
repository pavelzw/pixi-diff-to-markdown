# ruff: noqa: UP007
from sys import stdin
from typing import Annotated, Optional

import typer

from pixi_diff_to_markdown.diff import generate_output
from pixi_diff_to_markdown.models import Environments
from pixi_diff_to_markdown.settings import Settings, SplitTables

app = typer.Typer()


@app.command(
    help="Convert `pixi update --json` diff to markdown. Reads from stdin and writes to stdout: `pixi --json | pixi diff-to-markdown > output.md`"
)
def main(
    change_type_column: Annotated[
        Optional[bool],
        typer.Option(help="Enable the change type column.", show_default=False),
    ] = None,
    package_type_column: Annotated[
        Optional[bool],
        typer.Option(
            help="Enable the package type (conda/pypi) column.", show_default=False
        ),
    ] = None,
    explicit_column: Annotated[
        Optional[bool],
        typer.Option(
            help="Enable the explicit (explicit/implicit) column.", show_default=False
        ),
    ] = None,
    split_tables: Annotated[
        Optional[SplitTables],
        typer.Option(help="In what way to split tables.", show_default=False),
    ] = None,
    hide_tables: Annotated[
        Optional[bool],
        typer.Option(
            help="Whether to hide tables in a collapsible element.", show_default=False
        ),
    ] = None,
):
    settings_dict = {
        "change-type-column": change_type_column,
        "package-type-column": package_type_column,
        "explicit-column": explicit_column,
        "split-tables": split_tables,
        "hide-tables": hide_tables,
    }
    settings = Settings.model_validate(
        {k: v for k, v in settings_dict.items() if v is not None}
    )
    data = "".join(stdin.readlines())
    data_parsed = Environments.model_validate_json(data)
    output = generate_output(data_parsed, settings)
    print(output)
