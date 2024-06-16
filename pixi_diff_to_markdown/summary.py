from pixi_diff_to_markdown.environments_to_string import SupportMatrix
from pixi_diff_to_markdown.models import Environments, UpdatedEnvironments, UpdateSpec
from pixi_diff_to_markdown.settings import Settings





def generate_output_merged(data: Environments, settings: Settings) -> str:
    merged_update_specs = merge_update_specs(data)
    sorted_update_specs = sorted(
        [
            (update_spec, environments)
            for update_spec, environments in merged_update_specs.items()
        ],
        key=lambda x: x[0],
    )
    all_environments = list(data.root.keys())
    all_platforms = set()
    for environments in data.root.values():
        all_platforms |= set(environments.root.keys())
    all_platforms = list(all_platforms)
    lines = []
    lines.append(f"{generate_header(split_type="platform", settings=settings)} - |")
    for update_spec, environments in sorted_update_specs:
        support_matrix = SupportMatrix(environments, all_environments, all_platforms)
        updated_envs_str = support_matrix.get_str_representation()
        lines.append(
            f"{update_spec_to_table_line(update_spec, settings)} {updated_envs_str} |"
        )
    return "\n".join(lines)
