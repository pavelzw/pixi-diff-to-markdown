from pixi_diff_to_markdown.environments_to_string import SupportMatrix
from pixi_diff_to_markdown.models import (
    DependencyTable,
    DependencyType,
    Environments,
    TableRow,
    UpdateSpec,
    UpdatedEnvironments,
)
from pixi_diff_to_markdown.settings import Settings



def generate_output(data: Environments, settings: Settings) -> str:
    if settings.split_tables == "no":
        return generate_table_no_split_tables(data, settings)
    elif settings.split_tables == "environment":
        return generate_table_environment_split_tables(data, settings)
    elif settings.split_tables == "platform":
        return generate_table_platform_split_tables(data, settings)
    elif settings.split_tables == "merge":
        return generate_table_environment_merge_tables(data, settings)
    else:
        assert settings.split_tables == "merge-split-explicit"
        return generate_table_environment_merge_tables_split_explicit(data, settings)


def generate_footnotes() -> str:
    return """[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
"""


def generate_table_no_split_tables(data: Environments, settings: Settings) -> str:
    dependency_table = data.to_table(settings)
    table = dependency_table.to_string(settings)

    footnote = generate_footnotes()
    return table + "\n\n" + footnote


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


def merge_update_specs(data: Environments) -> dict[UpdateSpec, UpdatedEnvironments]:
    update_specs: dict[UpdateSpec, UpdatedEnvironments] = {}
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            for update_spec in dependencies.root:
                update_specs.setdefault(update_spec, []).append((environment, platform))
    return update_specs


def generate_table_environment_merge_tables(
    data: Environments, settings: Settings
) -> str:
    merged_update_specs = merge_update_specs(data)
    # TODO: ordereddict
    sorted_update_specs = sorted(
        [
            (update_spec, environments)
            for update_spec, environments in merged_update_specs.items()
        ],
        key=lambda x: x[0],
    )
    all_environments = list(data.root.keys())
    all_platforms_set = set()
    # TODO: reduce union
    for environments in data.root.values():
        all_platforms_set |= set(environments.root.keys())
    all_platforms = list(all_platforms_set)
    rows = []
    for update_spec, environments in sorted_update_specs:
        support_matrix = SupportMatrix(environments, all_environments, all_platforms)
        updated_envs_str = support_matrix.get_str_representation()
        rows.append(TableRow(update_spec, updated_environments=updated_envs_str))
    dependency_table = DependencyTable(rows, use_updated_environment_column=True)
    table_str = dependency_table.to_string(settings)
    footnote = generate_footnotes()
    return table_str + "\n\n" + footnote


def generate_table_environment_merge_tables_split_explicit(
    data: Environments, settings: Settings
) -> str:
    merged_update_specs = merge_update_specs(data)
    # TODO: ordereddict
    sorted_update_specs_explicit = sorted(
        [
            (update_spec, environments)
            for update_spec, environments in merged_update_specs.items() if update_spec.explicit == DependencyType.EXPLICIT
        ],
        key=lambda x: x[0],
    )
    sorted_update_specs_implicit = sorted(
        [
            (update_spec, environments)
            for update_spec, environments in merged_update_specs.items() if update_spec.explicit == DependencyType.IMPLICIT
        ],
        key=lambda x: x[0],
    )
    all_environments = list(data.root.keys())
    all_platforms_set = set()
    # TODO: reduce union
    for environments in data.root.values():
        all_platforms_set |= set(environments.root.keys())
    all_platforms = list(all_platforms_set)

    lines = []
    for dependency_type, sorted_update_specs in [
        ("Explicit", sorted_update_specs_explicit),
        ("Implicit", sorted_update_specs_implicit),
    ]:
        # TODO: make collapsible as well
        rows = []
        for update_spec, environments in sorted_update_specs:
            support_matrix = SupportMatrix(environments, all_environments, all_platforms)
            updated_envs_str = support_matrix.get_str_representation()
            rows.append(TableRow(update_spec, updated_environments=updated_envs_str))
        dependency_table = DependencyTable(rows, use_updated_environment_column=True)
        table_str = dependency_table.to_string(settings)
        lines.append(f"## {dependency_type} dependencies")
        lines.append("")
        lines.append(table_str)
        lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    return content + "\n" + footnote
