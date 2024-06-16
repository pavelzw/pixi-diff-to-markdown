from dataclasses import dataclass

import more_itertools


@dataclass(frozen=True)
class Cover:
    environments: frozenset[str]
    platforms: frozenset[str]

    def get_loss(self, all_environments: list[str], all_platforms: list[str]) -> float:
        return len(self.get_str_representation(all_environments, all_platforms))

    def get_str_representation(self, all_environments: list[str], all_platforms: list[str]) -> str:
        if len(self.environments) == len(all_environments) and len(self.platforms) == len(all_platforms):
            return "all"
        if len(self.environments) == len(all_environments):
            environments_str = "all envs"
        elif len(self.environments) == 1:
            environments_str, = self.environments
        else:
            environments_str = f"{{{', '.join(sorted(list(self.environments)))}}}"
        if len(self.platforms) == len(all_platforms):
            platforms_str = "all platforms"
        elif len(self.platforms) == 1:
            platforms_str, = self.platforms
        else:
            platforms_str = f"{{{', '.join(sorted(list(self.platforms)))}}}"
        return f"{environments_str} on {platforms_str}"


class SupportMatrix:
    """
    A list of environment / platform combination that were updated by a package.
    """
    all_environments: list[str]
    all_platforms: list[str]
    active_matrix: list[list[bool]]

    def __init__(self, active_elements: list[tuple[str, str]], all_environments: list[str], all_platforms: list[str]):
        self.all_environments = all_environments
        self.all_platforms = all_platforms
        self.active_matrix = [[False for _ in all_platforms] for _ in all_environments]
        for environment, platform in active_elements:
            self.active_matrix[all_environments.index(environment)][all_platforms.index(platform)] = True
    

    def get_environments_for_platform(self, platform: str) -> frozenset[str]:
        platform_index = self.all_platforms.index(platform)
        return frozenset(environment for environment, is_active in zip(self.all_environments, self.active_matrix) if is_active[platform_index])


    def merge_covers(self, covers: set[Cover]) -> set[Cover]:
        """
        merge all covers into one row-whise
        output all residues and the merged cover as new covers
        """
        # get all environments that are covered by every cover
        common_environments = set(self.all_environments)
        for cover in covers:
            common_environments &= set(cover.environments)
        if not common_environments:
            # unmergeable
            return covers
        platforms = set()
        for cover in covers:
            platforms |= set(cover.platforms)
        merged = Cover(frozenset(common_environments), frozenset(platforms))
        residues = set()
        for cover in covers:
            missing_environments = cover.environments - common_environments
            if missing_environments:
                residues.add(Cover(
                    missing_environments,
                    cover.platforms
                ))
        return residues | {merged}


    def find_optimal_cover(self) -> set[Cover]:
        # start out with all all columns as groups
        # then merge the groups with the best score
        # repeat until we cannot find a better merge greedily
        covers: set[Cover] = {
            Cover(self.get_environments_for_platform(platform), frozenset({platform}))
            for platform in self.all_platforms if self.get_environments_for_platform(platform)
        }
        score = sum(cover.get_loss(self.all_environments, self.all_platforms) for cover in covers)

        while True:
            minimal_score = score
            best_merge = None
            if len(covers) == 1:
                break
            powersets = more_itertools.powerset_of_sets(covers)
            for subset in powersets:
                if len(subset) < 2:
                    continue
                merged_cover = self.merge_covers(subset)
                unused_covers = covers - subset
                new_score = sum(cover.get_loss(self.all_environments, self.all_platforms) for cover in merged_cover) + sum(cover.get_loss(self.all_environments, self.all_platforms) for cover in unused_covers)
                if new_score < minimal_score:
                    minimal_score = new_score
                    best_merge = merged_cover | unused_covers
            if best_merge:
                covers = best_merge
                score = minimal_score
            else:
                break
        return covers

    def get_str_representation(self, covers: set[Cover] | None = None) -> str:
        if covers is None:
            covers = self.find_optimal_cover()
        return ", ".join(cover.get_str_representation(self.all_environments, self.all_platforms) for cover in covers)
