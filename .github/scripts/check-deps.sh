#!/usr/bin/env bash

set -euo pipefail

contains_dependency_all=true

while read -r package version; do
    if [[ $package == "python" ]]; then
        continue
    fi

    if [[ $package == "ordered_enum" ]]; then
        package="ordered-enum"
    fi

    dependency="${package} ${version}"

    contains_dependency=$(yq -r ".project.dependencies | map(. == \"${dependency}\") | any" pyproject.toml)
    if [[ $contains_dependency == "false" ]]; then
        echo "${dependency} not found in pyproject.toml"
        contains_dependency_all=false
    fi
done < <(yq -r '.dependencies | to_entries | .[] | "\(.key) \(.value)"' pixi.toml)

if [[ $contains_dependency_all == "false" ]]; then
    exit 1
fi
