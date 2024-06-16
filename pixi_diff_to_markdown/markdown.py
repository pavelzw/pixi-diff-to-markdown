from typing import Literal

def generate_table_line(*columns: str) -> str:
    return "|" + "|".join(columns) + "|"

def generate_markdown_table_header(columns: list[str], orientations: list[Literal["left", "right", "center"]]) -> str:
    assert len(columns) == len(orientations)
    first_line = "|" + "|".join(columns) + "|"
    orientation_mapping = {"left": "-", "right": "-:", "center": ":-:"}
    second_line = "|" + "|".join(orientation_mapping[orientation] for orientation in orientations) + "|"
    return first_line + "\n" + second_line
