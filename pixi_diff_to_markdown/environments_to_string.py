from dataclasses import dataclass
from functools import cache, reduce

import more_itertools

from pixi_diff_to_markdown.models import UpdatedEnvironments


@dataclass(frozen=True)
class Cover:
    environments: frozenset[str]
    platforms: frozenset[str]

    def objective(self, all_environments: set[str], all_platforms: set[str]) -> int:
        return len(self.get_str_representation(all_environments, all_platforms))

    def get_str_representation(
        self, all_environments: set[str], all_platforms: set[str]
    ) -> str:
        if len(self.environments) == len(all_environments) and len(
            self.platforms
        ) == len(all_platforms):
            return "*all*"
        if len(self.environments) == len(all_environments):
            environments_str = "*all envs*"
        elif len(self.environments) == 1:
            (environments_str,) = self.environments
        else:
            environments_str = f"{{{', '.join(sorted(list(self.environments)))}}}"
        if len(self.platforms) == len(all_platforms):
            platforms_str = "*all platforms*"
        elif len(self.platforms) == 1:
            (platforms_str,) = self.platforms
        else:
            platforms_str = f"{{{', '.join(sorted(list(self.platforms)))}}}"
        return f"{environments_str} on {platforms_str}"

    def __len__(self) -> int:
        return len(self.environments) * len(self.platforms)

    def __lt__(self, other: "Cover") -> bool:
        return len(self) < len(other)

    def __eq__(self, other: object) -> bool:
        # this is a hack to allow better sorting
        # this is not a total order but a total quasi-order
        # `sorted` needs `__eq__` to be consistent with `__lt__` in order for sorting tuples to work
        if not isinstance(other, Cover):
            return NotImplemented
        return len(self) == len(other)


class SupportMatrix:
    """
    A list of environment / platform combination that were updated by a package.
    """

    all_environments: set[str]
    all_platforms: set[str]
    platforms: dict[str, frozenset[str]]

    def __init__(
        self,
        active_elements: UpdatedEnvironments,
        all_environments: set[str],
        all_platforms: set[str],
    ):
        self.all_environments = all_environments
        self.all_platforms = all_platforms
        platforms_set: dict[str, set[str]] = {p: set() for p in all_platforms}
        for environment, platform in active_elements:
            platforms_set[platform].add(environment)

        self.platforms = {k: frozenset(v) for k, v in platforms_set.items()}

    def merge_covers(self, covers: set[Cover]) -> set[Cover]:
        """
        Construct one cover that includes all common elements of all covers.
        The remaining elements are put into separate covers.
        For each input cover, all elements that are not included in the common elements form a residual cover.
        Returns the set of all residual covers and the merged cover.

        If there are no common elements, the input covers are returned unchanged.
        """
        # get all environments that are covered by every cover
        assert len(covers) > 0
        common_environments = reduce(
            set.intersection, (set(cover.environments) for cover in covers)
        )
        if not common_environments:
            # unmergeable
            return covers
        platforms = reduce(set.union, (set(cover.platforms) for cover in covers))
        merged = Cover(frozenset(common_environments), frozenset(platforms))
        residuals = set()
        for cover in covers:
            missing_environments = cover.environments - common_environments
            if missing_environments:
                residuals.add(Cover(missing_environments, cover.platforms))
        return residuals | {merged}

    @cache
    def find_optimal_cover(self) -> set[Cover]:
        # start out with all all columns as groups
        # then merge the groups with the best objective
        # repeat until we cannot find a better merge greedily
        covers = {
            Cover(self.platforms[platform], frozenset((platform,)))
            for platform in self.all_platforms
            if self.platforms[platform]
        }

        def covers_objective(covers: set[Cover]) -> int:
            return sum(
                cover.objective(self.all_environments, self.all_platforms)
                for cover in covers
            )

        objective = covers_objective(covers)

        while True:
            minimal_objective = objective
            best_merge = None
            for subset in more_itertools.powerset_of_sets(covers):
                if len(subset) < 2:
                    continue
                # merged_covers = common cover + residuals
                merged_covers = self.merge_covers(subset)
                unmerged_covers = covers - subset
                new_covers = merged_covers | unmerged_covers
                new_objective = covers_objective(new_covers)
                if new_objective < minimal_objective:
                    minimal_objective = new_objective
                    best_merge = new_covers
            if best_merge:
                covers = best_merge
                objective = minimal_objective
            else:
                # no merge yielded any improvement
                break
        return covers

    def get_str_representation(self, covers: set[Cover] | None = None) -> str:
        if covers is None:
            covers = self.find_optimal_cover()
        covers_with_str = sorted(
            (
                (
                    cover,
                    cover.get_str_representation(
                        self.all_environments, self.all_platforms
                    ),
                )
                for cover in covers
            ),
            reverse=True,
        )
        return "<br/>".join(cover_str for _, cover_str in covers_with_str)

    def __str__(self) -> str:
        return self.get_str_representation()

    def __len__(self) -> int:
        return sum(len(cover) for cover in self.find_optimal_cover())
