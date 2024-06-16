from pixi_diff_to_markdown.models import (
    ChangeType,
    DependencyType,
    Environments,
    UpdateSpec,
)
from pixi_diff_to_markdown.settings import Settings, SplitTables



def generate_output(data: Environments, settings: Settings) -> str:
    if settings.split_tables == "no":
        return generate_table_no_split_tables(data, settings)
    elif settings.split_tables == "environment":
        return generate_table_environment_split_tables(data, settings)
    else:
        assert settings.split_tables == "platform"
        return generate_table_platform_split_tables(data, settings)


def generate_footnotes() -> str:
    return """[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
"""


def generate_table_no_split_tables(data: Environments, settings: Settings) -> str:
    dependency_table = data.to_table(settings)
    table = dependency_table.to_string(settings)

    footnote = generate_footnotes()
    table = table + "\n\n" + footnote
    return table


def generate_table_environment_split_tables(
    data: Environments, settings: Settings
) -> str:
    lines = []
    for environment, platforms in data.root.items():
        if settings.hide_tables:
            lines.append("<details>")
            lines.append(f"<summary>{environment}</summary>")
        else:
            lines.append(f"## {environment}")
        lines.append("")

        dependency_table = platforms.to_table(settings)
        lines.append(dependency_table.to_string(settings))
        if settings.hide_tables:
            lines.append("")
            lines.append("</details>")
        lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table


def generate_table_platform_split_tables(data: Environments, settings: Settings) -> str:
    lines = []
    for environment, platforms in data.root.items():
        lines.append(f"# {environment}")
        lines.append("")
        for platform, dependencies in platforms.root.items():
            if settings.hide_tables:
                lines.append("<details>")
                lines.append(f"<summary>{platform}</summary>")
            else:
                lines.append(f"## {platform}")
            lines.append("")
            dependency_table = dependencies.to_table(settings)
            lines.append(dependency_table.to_string(settings))
            if settings.hide_tables:
                lines.append("")
                lines.append("</details>")
            lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table
