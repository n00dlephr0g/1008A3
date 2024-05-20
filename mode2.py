from mode1 import *


class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
        :complexity best: 
        :complexity best: 
        :complexity worst:
    """

    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.teamCount = n_teams
        self.sites: list[Land] = []


    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        for site in sites:
            if site.get_reward() < 2/5:
                self.sites.append(site)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        for team in range(self.teamCount):
            pass

