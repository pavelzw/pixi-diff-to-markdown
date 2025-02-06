from functools import cmp_to_key, reduce

from pixi_diff_to_markdown.environments_to_string import SupportMatrix
from pixi_diff_to_markdown.models import (
    DependencyTable,
    DependencyType,
    Environments,
    TableRow,
    UpdatedEnvironments,
    UpdateSpec,
)
from pixi_diff_to_markdown.settings import HideTables, MergeDependencies, Settings


def generate_output(data: Environments, settings: Settings) -> str:
    if not data.root:
        return ""
    if settings.merge_dependencies == MergeDependencies.no:
        return generate_table_no_merge(data, settings)
    elif settings.merge_dependencies == MergeDependencies.yes:
        return generate_table_merge_all(data, settings)
    else:
        assert settings.merge_dependencies == MergeDependencies.split_explicit
        return generate_table_split_explicit(data, settings)


def generate_footnotes() -> str:
    return """[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.
"""


def details_opener(open: bool) -> str:
    return "<details open>" if open else "<details>"


def generate_table_no_merge(data: Environments, settings: Settings) -> str:
    longest_table = max(
        len(dependencies)
        for platforms in data.root.values()
        for dependencies in platforms.root.values()
    )
    collapsible_tables = settings.hide_tables == HideTables.yes or (
        settings.hide_tables == HideTables.auto
        and longest_table > settings.max_expanded_rows
    )
    lines = []
    for environment, platforms in data.root.items():
        lines.append(f"# {environment}")
        lines.append("")
        for platform, dependencies in platforms.root.items():
            if collapsible_tables:
                lines.append(
                    details_opener(len(dependencies) <= settings.max_expanded_rows),
                )
                lines.append(f"<summary>{platform}</summary>")
            else:
                lines.append(f"## {platform}")
            lines.append("")
            dependency_table = dependencies.to_table()
            lines.append(dependency_table.to_string(settings))
            if collapsible_tables:
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


def get_sorted_update_specs(data: Environments) -> list[tuple[UpdateSpec, str]]:
    def compare_merged_update_specs(
        a: tuple[UpdateSpec, int, str],
        b: tuple[UpdateSpec, int, str],
    ) -> int:
        """
        Custom sorting for merged update specs.
        1. Sort by explicit
        2. Sort by change type
        3. Sort by name
        4. Sort by after string (descending)
        5. Sort by number of environments (descending)
        6. Sort by before string (ascending)
        7. Sort by package type
        """

        def cmp(a, b) -> int:
            return (a > b) - (a < b)

        if a[0].explicit != b[0].explicit:
            return cmp(a[0].explicit, b[0].explicit)
        if a[0].change_type != b[0].change_type:
            return cmp(a[0].change_type, b[0].change_type)
        if a[0].name != b[0].name:
            return cmp(a[0].name, b[0].name)
        a_before, a_after = a[0].before_after_str()
        b_before, b_after = b[0].before_after_str()
        if a_after != b_after:
            return cmp(b_after, a_after)
        if a[1] != b[1]:
            return cmp(b[1], a[1])
        if a_before != b_before:
            return cmp(a_before, b_before)
        if a[0].type != b[0].type:
            return cmp(a[0].type, b[0].type)
        return 0

    all_environments = set(data.root.keys())
    all_platforms: set[str] = reduce(
        set.union,
        (set(environments.root.keys()) for environments in data.root.values()),
        set(),
    )
    merged_update_specs = merge_update_specs(data)
    update_specs_with_envs = []
    for update_spec, environments in merged_update_specs.items():
        support_matrix = SupportMatrix(environments, all_environments, all_platforms)
        updated_envs_str = support_matrix.get_str_representation()
        update_specs_with_envs.append(
            (update_spec, len(support_matrix), updated_envs_str)
        )
    sorted_update_specs = sorted(
        update_specs_with_envs, key=cmp_to_key(compare_merged_update_specs)
    )
    return [
        (update_spec, updated_envs_str)
        for update_spec, _, updated_envs_str in sorted_update_specs
    ]


def generate_table_merge_all(data: Environments, settings: Settings) -> str:
    rows = [
        TableRow(update_spec, updated_environments=updated_envs_str)
        for update_spec, updated_envs_str in get_sorted_update_specs(data)
    ]
    dependency_table = DependencyTable(rows, use_updated_environment_column=True)
    table_str = dependency_table.to_string(settings)
    if settings.hide_tables == HideTables.yes or (
        settings.hide_tables == HideTables.auto
        and len(rows) > settings.max_expanded_rows
    ):
        table_str = "\n".join(
            [
                details_opener(len(rows) <= settings.max_expanded_rows),
                "<summary>Dependencies</summary>",
                "",
                table_str,
                "",
                "</details>",
            ]
        )
    footnote = generate_footnotes()
    return table_str + "\n\n" + footnote


def generate_table_split_explicit(data: Environments, settings: Settings) -> str:
    # TODO: ordereddict
    sorted_update_specs = get_sorted_update_specs(data)
    update_specs_explicit = list(
        filter(lambda x: x[0].explicit == DependencyType.EXPLICIT, sorted_update_specs)
    )
    update_specs_implicit = list(
        filter(lambda x: x[0].explicit == DependencyType.IMPLICIT, sorted_update_specs)
    )
    collapsible_tables = settings.hide_tables == HideTables.yes or (
        settings.hide_tables == HideTables.auto
        and max(len(update_specs_explicit), len(update_specs_implicit))
        > settings.max_expanded_rows
    )

    lines = []
    if collapsible_tables:
        lines.append("# Dependencies\n")

    for dependency_type, update_specs in [
        ("Explicit", update_specs_explicit),
        ("Implicit", update_specs_implicit),
    ]:
        rows = [
            TableRow(update_spec, updated_environments=updated_envs_str)
            for update_spec, updated_envs_str in update_specs
        ]
        dependency_table = DependencyTable(rows, use_updated_environment_column=True)
        table_str = dependency_table.to_string(settings)
        if collapsible_tables:
            lines.append(
                details_opener(len(rows) <= settings.max_expanded_rows),
            )
            lines.append(f"<summary>{dependency_type} dependencies</summary>\n")
        else:
            lines.append(f"# {dependency_type} dependencies\n")
        lines.append(table_str)
        if collapsible_tables:
            lines.append("")
            lines.append("</details>")
        lines.append("")
    content = "\n".join(lines)
    footnote = generate_footnotes()
    return content + "\n" + footnote
