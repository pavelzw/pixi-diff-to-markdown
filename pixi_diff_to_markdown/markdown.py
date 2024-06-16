def generate_table_line(*columns: str) -> str:
    return "|" + "|".join(columns) + "|"


def generate_markdown_table_header(columns: list[str]) -> str:
    first_line = "|" + "|".join(columns) + "|"
    second_line = "|-" * len(columns) + "|"
    return first_line + "\n" + second_line
