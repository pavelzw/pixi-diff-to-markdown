from itertools import product

import pytest

from pixi_diff_to_markdown.environments_to_string import Cover, SupportMatrix

all_environments = ["default", "py39", "py310", "py311", "py312"]
all_platforms = [
    "linux-64",
    "linux-aarch64",
    "linux-ppc64le",
    "osx-arm64",
    "osx-64",
    "win-64",
]


# TODO: merge linux-64 and linux-aarch64 and linux-ppc64le into linux if possible
@pytest.mark.parametrize(
    "environments,platforms,expected",
    [
        (
            ["py39", "py310", "py311"],
            ["linux-64", "osx-arm64"],
            "{py310, py311, py39} on {linux-64, osx-arm64}",
        ),
        (["py39", "py310", "py311"], ["linux-64"], "{py310, py311, py39} on linux-64"),
        (["py39"], ["linux-64", "osx-arm64"], "py39 on {linux-64, osx-arm64}"),
        (["py39"], ["linux-64"], "py39 on linux-64"),
        (all_environments, ["linux-64"], "*all envs* on linux-64"),
        (
            all_environments,
            ["linux-64", "osx-arm64"],
            "*all envs* on {linux-64, osx-arm64}",
        ),
        (["py39"], all_platforms, "py39 on *all platforms*"),
        (all_environments, all_platforms, "*all*"),
    ],
)
def test_str_representation(
    environments: list[str], platforms: list[str], expected: str
):
    cover = Cover(
        frozenset(environments),
        frozenset(platforms),
    )
    assert (
        cover.get_str_representation(set(all_environments), set(all_platforms))
        == expected
    )


@pytest.mark.parametrize(
    "active_matrix,environments_for_platform,str_representation",
    [
        (
            [
                [False, False, False, False, False, False],  # default
                [True, False, False, False, False, False],  # py39
                [True, False, False, False, False, False],  # py310
                [True, False, False, True, False, False],  # py311
                [True, False, False, False, False, True],  # py312
            ],
            {
                "linux-64": {"py39", "py310", "py311", "py312"},
                "linux-aarch64": set(),
                "linux-ppc64le": set(),
                "osx-arm64": {"py311"},
                "osx-64": set(),
                "win-64": {"py312"},
            },
            "{py310, py311, py312, py39} on linux-64<br/>py312 on win-64<br/>py311 on osx-arm64",
        ),
        (
            [
                [True, True, True, True, True, True],  # default
                [True, True, True, True, True, False],  # py39
                [True, True, True, True, False, True],  # py310
                [True, False, False, True, False, True],  # py311
                [True, False, False, False, False, True],  # py312
            ],
            {
                "linux-64": {"default", "py39", "py310", "py311", "py312"},
                "linux-aarch64": {"default", "py39", "py310"},
                "linux-ppc64le": {"default", "py39", "py310"},
                "osx-arm64": {"default", "py39", "py310", "py311"},
                "osx-64": {"default", "py39"},
                "win-64": {"default", "py310", "py311", "py312"},
            },
            "{default, py310, py39} on {linux-aarch64, linux-ppc64le, osx-arm64}<br/>*all envs* on linux-64<br/>{default, py310, py311, py312} on win-64<br/>{default, py39} on osx-64<br/>py311 on osx-arm64",
        ),
    ],
)
def test_support_matrix(
    active_matrix: list[list[bool]],
    environments_for_platform: dict[str, list[str]],
    str_representation: str,
):
    active_elements = []
    for (i, environment), (j, platform) in product(
        enumerate(all_environments), enumerate(all_platforms)
    ):
        if active_matrix[i][j]:
            active_elements.append((environment, platform))
    support_matrix = SupportMatrix(
        active_elements, set(all_environments), set(all_platforms)
    )

    for platform, environments in environments_for_platform.items():
        assert support_matrix.platforms[platform] == environments
    assert str(support_matrix) == str_representation
