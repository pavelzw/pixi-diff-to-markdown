#!/usr/bin/env bash

set -euo pipefail

contains_dependency_all=true

while read -r package version; do
    if [[ $package == "python" ]]; then
        continue
    fi

    dependency="${package} ${version}"

    contains_dependency=$(yq -r ".project.dependencies | map(. == \"${dependency}\") | any" pyproject.toml)
    if [[ $contains_dependency == "false" ]]; then
        echo "${dependency} not found in pyproject.toml"
        contains_dependency_all=false
    fi
done < <(yq -r '.package.run-dependencies | to_entries | .[] | "\(.key) \(.value)"' pixi.toml)

if [[ $contains_dependency_all == "false" ]]; then
    exit 1
fi

if [[ $(yq -r ".package.version" pixi.toml) != $(yq -r ".project.version" pyproject.toml) ]]; then
    echo "package version in pixi.toml does not match project version in pyproject.toml"
    exit 1
fi
