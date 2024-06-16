from typing import Literal

from pixi_diff_to_markdown.markdown import generate_table_line
from pixi_diff_to_markdown.models import (
    ChangeType,
    DependencyType,
    Environments,
    UpdateSpec,
    calculate_change_type,
)
from pixi_diff_to_markdown.settings import Settings, SplitTables


def update_spec_to_table_line(update_spec: UpdateSpec, settings: Settings) -> list[str]:
    change_type = calculate_change_type(update_spec)
    before: str | None
    after: str | None
    if change_type == ChangeType.ADDED:
        before = ""
        after = update_spec.after.version  # type: ignore[union-attr]
    elif change_type == ChangeType.REMOVED:
        before = update_spec.before.version  # type: ignore[union-attr]
        after = ""
    elif change_type == ChangeType.BUILD:
        before = update_spec.before.build  # type: ignore[union-attr]
        after = update_spec.after.build  # type: ignore[union-attr]
    else:
        before = update_spec.before.version  # type: ignore[union-attr]
        after = update_spec.after.version  # type: ignore[union-attr]
    assert before is not None
    assert after is not None

    if (
        change_type == ChangeType.MAJOR_DOWN
        or change_type == ChangeType.MINOR_DOWN
        or change_type == ChangeType.PATCH_DOWN
    ):
        maybe_downgrade_ref = "[^2]"
    else:
        maybe_downgrade_ref = ""
    add_explicit = settings.explicit_column
    add_change_type = settings.change_type_column
    add_package_type = settings.package_type_column
    if not add_explicit and update_spec.explicit == DependencyType.EXPLICIT:
        package_name_formatted = f"*{update_spec.name}*"
    else:
        package_name_formatted = update_spec.name

    columns = [
        package_name_formatted + maybe_downgrade_ref,
        before,
        after,
        *([change_type.value] if add_change_type else []),
        *([str(update_spec.explicit == DependencyType.EXPLICIT).lower()] if add_explicit else []),
        *([update_spec.type] if add_package_type else []),
    ]
    return generate_table_line(*columns)


def generate_output(data: Environments, settings: Settings) -> str:
    if settings.split_tables == "no":
        return generate_table_no_split_tables(data, settings)
    elif settings.split_tables == "environment":
        return generate_table_environment_split_tables(data, settings)
    else:
        assert settings.split_tables == "platform"
        return generate_table_platform_split_tables(data, settings)


def generate_header(
    settings: Settings
):
    add_change_type = settings.change_type_column
    add_explicit = settings.explicit_column
    add_package_type = settings.package_type_column
    if settings.split_tables == SplitTables.no:
        prefix = "| Environment "
    elif settings.split_tables == SplitTables.environment:
        prefix = "| Platform "
    else:
        assert settings.split_tables == SplitTables.platform
        prefix = ""
    header_line1 = (
        f"{prefix}| Dependency{"[^1]" if not add_explicit else ""} | Before | After |"
        f"{" Change |" if add_change_type else ""}"
        f"{" Explicit |" if add_explicit else ""}"
        f"{" Package |" if add_package_type else ""}"
    )
    header_line2 = f"{"| -: " if settings.split_tables != SplitTables.platform else ""}| - | - | - |{" - |" if add_change_type else ""}{" - |" if add_explicit else ""}{" - |" if add_package_type else ""}"
    return header_line1 + "\n" + header_line2


def generate_footnotes() -> str:
    return """[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
"""


def generate_table_no_split_tables(data: Environments, settings: Settings) -> str:
    header = generate_header(settings)
    lines = []
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            lines_platform = [
                update_spec_to_table_line(update_spec, settings)
                for update_spec in sorted(dependencies.root)
            ]
            lines_platform[0] = f"| {environment} / {platform} {lines_platform[0]}"
            for i in range(1, len(lines_platform)):
                lines_platform[i] = "|" + lines_platform[i]
            lines.extend(lines_platform)
    lines.append("")
    content = "\n".join(lines)

    footnote = generate_footnotes()
    table = header + "\n" + content + "\n" + footnote
    return table


def generate_table_environment_split_tables(
    data: Environments, settings: Settings
) -> str:
    header = generate_header(settings)
    lines = []
    for environment, platforms in data.root.items():
        if settings.hide_tables:
            lines.append("<details>")
            lines.append(f"<summary>{environment}</summary>")
        else:
            lines.append(f"## {environment}")
        lines.append("")
        lines.append(header)
        for platform, dependencies in platforms.root.items():
            lines_platform = [
                update_spec_to_table_line(update_spec, settings)
                for update_spec in sorted(dependencies.root)
            ]
            lines_platform[0] = f"| {platform} {lines_platform[0]}"
            for i in range(1, len(lines_platform)):
                lines_platform[i] = "|" + lines_platform[i]
            lines.extend(lines_platform)
        if settings.hide_tables:
            lines.append("")
            lines.append("</details>")
        lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table


def generate_table_platform_split_tables(data: Environments, settings: Settings) -> str:
    header = generate_header(settings)
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
            lines.append(header)
            lines_platform = [
                update_spec_to_table_line(update_spec, settings)
                for update_spec in sorted(dependencies.root)
            ]
            lines.extend(lines_platform)
            if settings.hide_tables:
                lines.append("")
                lines.append("</details>")
            lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table
