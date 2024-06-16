def generate_table_line(*columns: str) -> str:
    return "|" + "|".join(columns) + "|"

def generate_header(*columns: str) -> str:
    first_line = "|" + "|".join(columns) + "|"
    second_line = "|-" * len(columns) + "|"
    return first_line + "\n" + second_line


def generate_table(columns: list[str], lines: dict[str, list[str]]) -> str:
    header = generate_header(*columns)
    table_lines = []
    for i in range(len(lines[columns[0]])):
        table_lines.append(generate_table_line(*[lines[column][i] for column in columns]))
    return header + "\n" + "\n".join(table_lines) + "\n"
