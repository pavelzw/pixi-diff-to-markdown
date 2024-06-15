from pixi_diff_to_markdown.diff import generate_header, update_spec_to_table_line
from pixi_diff_to_markdown.models import Environments, UpdateSpec
from pixi_diff_to_markdown.settings import Settings

UpdatedEnvironments = list[tuple[str, str]]


def merge_update_specs(data: Environments) -> dict[UpdateSpec, UpdatedEnvironments]:
    update_specs = {}
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            for update_spec in dependencies.root:
                update_specs.setdefault(update_spec, []).append((environment, platform))
    return update_specs


def environments_to_str(environments: UpdatedEnvironments, data: Environments) -> str:
    # todo: make prettier
    # return "all"
    all_environments = []
    for environment, platforms in data.root.items():
        all_environments.extend([(environment, platform) for platform in platforms.root])
    if len(environments) == len(all_environments):
        return "all"
    
    all_by_environment = {}
    for environment, platform in all_environments:
        all_by_environment.setdefault(environment, []).append(platform)
    all_by_platform = {}
    for environment, platform in all_environments:
        all_by_platform.setdefault(platform, []).append(environment)

    by_environment = {}
    by_platform = {}
    for environment, platform in environments:
        by_environment.setdefault(environment, []).append(platform)
    for environment, platform in environments:
        by_platform.setdefault(platform, []).append(environment)
    
    # check if all environments are covered for only some platforms
    if all(
        len(by_platform[platform]) == len(all_by_platform[platform]) for platform in by_platform
    ):
        return f"all / {' '.join(by_platform.keys())}"

    environment_strings = []
    for environment, platforms in by_environment.items():
        all_platforms = [platform for platform in data.root[environment].root]
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
