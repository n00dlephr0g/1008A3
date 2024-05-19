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
        self.sites = []

    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites += sites

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        decision = 0
        Land.get_reward(adventurer_size - decision)

    # adventurers left = initial - sent
    # sent = initial - adventurers left
    def score(self,land,initial,adventurersLeft):
        return 2.5*adventurersLeft+land.get_reward(initial - adventurersLeft)