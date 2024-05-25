import json

from pixi_diff_to_markdown.models import Configuration, Environments, UpdateSpec

CONFIGURATION: Configuration = {
    "enable_change_column": True,
    "enable_package_type_column": True,
    "enable_explicit_implicit_column": True,
    "split_tables": "platform",
    "hide_tables": True,
}


def update_spec_to_table_line(
    package_name: str, update_spec: UpdateSpec, add_package_type: bool
) -> str:
    return f"| {package_name} | {update_spec.before.version} {update_spec.before.build} | {update_spec.after.version} {update_spec.after.build} |{f' {update_spec.type_} |' if add_package_type else ''}"


def generate_output(data: Environments) -> str:
    add_package_type = CONFIGURATION["enable_package_type_column"]
    if CONFIGURATION["split_tables"] == "no":
        return generate_table_no_split_tables(data, add_package_type)
    elif CONFIGURATION["split_tables"] == "environment":
        return generate_table_environment_split_tables(data, add_package_type)
    elif CONFIGURATION["split_tables"] == "platform":
        return generate_table_platform_split_tables(data, add_package_type)


def generate_table_no_split_tables(data: Environments, add_package_type: bool) -> str:
    header = f"""| Environment | Dependency | Before | After |{" Package |" if add_package_type else ""}
| -: | - | - | - |{" - |" if add_package_type else ""}"""
    lines = []
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            lines_platform = [
                update_spec_to_table_line(package_name, update_spec, add_package_type)
                for (package_name, update_spec) in dependencies.root.items()
            ]
            lines_platform[0] = f"| {environment} / {platform} {lines_platform[0]}"
            for i in range(1, len(lines_platform)):
                lines_platform[i] = "|" + lines_platform[i]
            lines.extend(lines_platform)
    content = "\n".join(lines)
    table = header + "\n" + content
    return table


def generate_table_environment_split_tables(
    data: Environments, add_package_type: bool
) -> str:
    header = f"""| Platform | Dependency | Before | After |{" Package |" if add_package_type else ""}
| -: | - | - | - |{" - |" if add_package_type else ""}"""
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
                update_spec_to_table_line(package_name, update_spec, add_package_type)
                for (package_name, update_spec) in dependencies.root.items()
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
    table = content
    return table


def generate_table_platform_split_tables(
    data: Environments, add_package_type: bool
) -> str:
    header = f"""| Dependency | Before | After |{" Package |" if add_package_type else ""}
| - | - | - |{" - |" if add_package_type else ""}"""
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
                update_spec_to_table_line(package_name, update_spec, add_package_type)
                for (package_name, update_spec) in dependencies.root.items()
            ]
            lines.extend(lines_platform)
            if CONFIGURATION["hide_tables"]:
                lines.append("")
                lines.append("</details>")
            lines.append("")
    content = "\n".join(lines)
    table = content
    return table


def main():
    with open("test.json") as f:
        data = json.load(f)
    data_parsed = Environments(data)
    print(generate_output(data_parsed))
    # with open("out.md","w") as f:
    #     f.writelines(generate_output(data_parsed))


if __name__ == "__main__":
    main()
