import json
from typing import Literal

import pydantic


class CondaVersion(pydantic.BaseModel):
    version: str
    build: str


class UpdateSpec(pydantic.BaseModel):
    before: CondaVersion
    after: CondaVersion
    type_: Literal["conda"]


def update_spec_to_table_line(x: UpdateSpec, package_name: str) -> str:
    return f"| {package_name} | {x.before.version} {x.before.build} | {x.after.version} {x.after.build} |"


def generate_table(x: dict[str, UpdateSpec]) -> str:
    header = """| Dependency | Before | After |
| - | - | - |"""
    pass
    lines = []
    for item in x:
        line = update_spec_to_table_line(x[item], item)
        lines.append(line)
    mystring = "\n".join(lines)
    table = header + "\n" + mystring
    return table


def main():
    with open("test.json") as f:
        data = json.load(f)
    env_dependencies = data["default"]["linux-64"]
    env_dependencies = {
        key: UpdateSpec(**value) for (key, value) in env_dependencies.items()
    }
    print(generate_table(env_dependencies))


if __name__ == "__main__":
    main()
