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


def update_spec_to_table_line(package_name: str, update_spec: UpdateSpec) -> str:
    return f"| {package_name} | {update_spec.before.version} {update_spec.before.build} | {update_spec.after.version} {update_spec.after.build} |"


def generate_table(x: dict[str, UpdateSpec]) -> str:
    header = """| Dependency | Before | After |
| - | - | - |"""
    lines = [
        update_spec_to_table_line(package_name, update_spec)
        for (package_name, update_spec) in x.items()
    ]
    content = "\n".join(lines)
    table = header + "\n" + content
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
