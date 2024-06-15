from pixi_diff_to_markdown.diff import generate_header, update_spec_to_table_line
from pixi_diff_to_markdown.models import Environments, UpdateSpec
from pixi_diff_to_markdown.settings import Settings

UpdatedEnvironments = dict[str, list[str]]


def merge_update_specs(data: Environments) -> dict[UpdateSpec, UpdatedEnvironments]:
    update_specs = {}
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            for update_spec in dependencies.root:
                if update_spec not in update_specs:
                    update_specs[update_spec] = {environment: [platform]}
                else:
                    if environment not in update_specs[update_spec]:
                        update_specs[update_spec][environment] = [platform]
                    else:
                        update_specs[update_spec][environment].append(platform)
    return update_specs


def get_platforms_for_environment(environment: str, data: Environments) -> list[str]:
    return [platform for platform in data.root[environment].root]


def environments_to_str(environments: UpdatedEnvironments, data: Environments) -> str:
    environment_strings = []
    for environment, platforms in environments.items():
        all_platforms = get_platforms_for_environment(environment, data)
        if len(platforms) == len(all_platforms):
            environment_strings.append(environment)
        elif len(platforms) == 1:
            environment_strings.append(f"{environment} / {platforms[0]}")
        else:
            environment_strings.append(f"{environment} / {" ".join(platforms)}")
    return ", ".join(environment_strings)


def generate_output_merged(data: Environments, settings: Settings) -> str:
    merged_update_specs = merge_update_specs(data)
    sorted_update_specs = sorted(
        [
            (update_spec, environments)
            for update_spec, environments in merged_update_specs.items()
        ],
        key=lambda x: x[0],
    )
    lines = []
    lines.append(f"{generate_header(split_type="platform", settings=settings)} - |")
    for update_spec, environments in sorted_update_specs:
        lines.append(
            f"{update_spec_to_table_line(update_spec, settings)} {environments_to_str(environments, data)} |"
        )
    return "\n".join(lines)
