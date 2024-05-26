import json
from typing import Literal

from pixi_diff_to_markdown.models import (
    ChangeType,
    Configuration,
    Environments,
    UpdateSpec,
    calculate_change_type,
)

CONFIGURATION: Configuration = {
    "enable_change_type_column": True,
    "enable_package_type_column": False,
    "enable_explicit_type_column": False,
    "split_tables": "no",
    "hide_tables": False,
}

# TODO: sort


def update_spec_to_table_line(
    package_name: str,
    update_spec: UpdateSpec,
    add_change_type: bool,
    add_explicit_type: bool,
    add_package_type: bool,
) -> str:
    change_type = calculate_change_type(update_spec)
    before = (
        update_spec.before.version
        if change_type != ChangeType.BUILD
        else update_spec.before.build
    )
    after = (
        update_spec.after.version
        if change_type != ChangeType.BUILD
        else update_spec.after.build
    )
    if (
        change_type == ChangeType.MAJOR_DOWN
        or change_type == ChangeType.MINOR_DOWN
        or change_type == ChangeType.PATCH_DOWN
    ):
        maybe_downgrade_ref = "[^2]"
    else:
        maybe_downgrade_ref = ""

    if not add_explicit_type and update_spec.explicit:
        package_name_formatted = f"*{package_name}*"
    else:
        package_name_formatted = package_name

    return (
        f"| {package_name_formatted + maybe_downgrade_ref} |"
        f" {before} |"
        f" {after} |"
        f"{f" {change_type.value} |" if add_change_type else ""}"
        f"{f" {str(update_spec.explicit).lower()} |" if add_explicit_type else ""}"
        f"{f' {update_spec.type_} |' if add_package_type else ''}"
    )


def generate_output(data: Environments) -> str:
    add_change_type = CONFIGURATION["enable_change_type_column"]
    add_explicit_type = CONFIGURATION["enable_explicit_type_column"]
    add_package_type = CONFIGURATION["enable_package_type_column"]
    if CONFIGURATION["split_tables"] == "no":
        return generate_table_no_split_tables(
            data, add_change_type, add_explicit_type, add_package_type
        )
    elif CONFIGURATION["split_tables"] == "environment":
        return generate_table_environment_split_tables(
            data, add_change_type, add_explicit_type, add_package_type
        )
    elif CONFIGURATION["split_tables"] == "platform":
        return generate_table_platform_split_tables(
            data, add_change_type, add_explicit_type, add_package_type
        )


def generate_header(
    split_type: Literal["no", "environment", "platform"],
    add_change_type: bool,
    add_explicit_type: bool,
    add_package_type: bool,
):
    if split_type == "no":
        prefix = "| Environment "
    elif split_type == "environment":
        prefix = "| Platform "
    else:
        assert split_type == "platform"
        prefix = ""
    header_line1 = (
        f"{prefix}| Dependency{"[^1]" if not add_explicit_type else ""} | Before | After |"
        f"{" Change |" if add_change_type else ""}"
        f"{" Explicit |" if add_explicit_type else ""}"
        f"{" Package |" if add_package_type else ""}"
    )
    header_line2 = f"{"| -: " if split_type != "platform" else ""}| - | - | - |{" - |" if add_change_type else ""}{" - |" if add_explicit_type else ""}{" - |" if add_package_type else ""}"
    return header_line1 + "\n" + header_line2


def generate_footnotes() -> str:
    return """[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
"""


def generate_table_no_split_tables(
    data: Environments,
    add_change_type: bool,
    add_explicit_type: bool,
    add_package_type: bool,
) -> str:
    header = generate_header("no", add_change_type, add_explicit_type, add_package_type)
    lines = []
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            lines_platform = [
                update_spec_to_table_line(
                    package_name,
                    update_spec,
                    add_change_type,
                    add_explicit_type,
                    add_package_type,
                )
                for (package_name, update_spec) in sorted(
                    dependencies.root.items(), key=lambda x: (x[1], x[0])
                )
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
    data: Environments,
    add_change_type: bool,
    add_explicit_type: bool,
    add_package_type: bool,
) -> str:
    header = generate_header(
        "environment", add_change_type, add_explicit_type, add_package_type
    )
    lines = []
    for environment, platforms in data.root.items():
        if CONFIGURATION["hide_tables"]:
            lines.append("<details>")
            lines.append(f"<summary>{environment}</summary>")
        else:
            lines.append(f"## {environment}")
        lines.append("")
        lines.append(header)
        for platform, dependencies in platforms.root.items():
            lines_platform = [
                update_spec_to_table_line(
                    package_name,
                    update_spec,
                    add_change_type,
                    add_explicit_type,
                    add_package_type,
                )
                for (package_name, update_spec) in sorted(
                    dependencies.root.items(), key=lambda x: (x[1], x[0])
                )
            ]
            lines_platform[0] = f"| {platform} {lines_platform[0]}"
            for i in range(1, len(lines_platform)):
                lines_platform[i] = "|" + lines_platform[i]
            lines.extend(lines_platform)
        if CONFIGURATION["hide_tables"]:
            lines.append("")
            lines.append("</details>")
        lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table


def generate_table_platform_split_tables(
    data: Environments,
    add_change_type: bool,
    add_explicit_type: bool,
    add_package_type: bool,
) -> str:
    header = generate_header(
        "platform", add_change_type, add_explicit_type, add_package_type
    )
    lines = []
    for environment, platforms in data.root.items():
        lines.append(f"# {environment}")
        lines.append("")
        for platform, dependencies in platforms.root.items():
            if CONFIGURATION["hide_tables"]:
                lines.append("<details>")
                lines.append(f"<summary>{platform}</summary>")
            else:
                lines.append(f"## {platform}")
            lines.append("")
            lines.append(header)
            lines_platform = [
                update_spec_to_table_line(
                    package_name,
                    update_spec,
                    add_change_type,
                    add_explicit_type,
                    add_package_type,
                )
                for (package_name, update_spec) in sorted(
                    dependencies.root.items(), key=lambda x: (x[1], x[0])
                )
            ]
            lines.extend(lines_platform)
            if CONFIGURATION["hide_tables"]:
                lines.append("")
                lines.append("</details>")
            lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    table = content + "\n" + footnote
    return table


def main():
    with open("test.json") as f:
        data = json.load(f)
    data_parsed = Environments(data)
    calculate_change_type(data_parsed.root["default"].root["linux-64"].root["polars"])
    print(generate_output(data_parsed))
    with open("out.md", "w") as f:
        f.writelines(generate_output(data_parsed))


if __name__ == "__main__":
    main()
