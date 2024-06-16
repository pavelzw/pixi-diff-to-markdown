from pixi_diff_to_markdown.diff import generate_header, update_spec_to_table_line
from pixi_diff_to_markdown.find_environments import environments_to_str
from pixi_diff_to_markdown.models import Environments, UpdatedEnvironments, UpdateSpec
from pixi_diff_to_markdown.settings import Settings


def merge_update_specs(data: Environments) -> dict[UpdateSpec, UpdatedEnvironments]:
    update_specs: dict[UpdateSpec, UpdatedEnvironments] = {}
    for environment, platforms in data.root.items():
        for platform, dependencies in platforms.root.items():
            for update_spec in dependencies.root:
                update_specs.setdefault(update_spec, []).append((environment, platform))
    return update_specs


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
