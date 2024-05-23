from landsites import *
from algorithms.mergesort import *

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
        :complexity best: 
        :complexity worst:
    """

    def __init__(self, n_teams: int) -> None:
        """
        __init__ initialises a game given a number of teams

        :param n_teams: an integer amount of teams
        :complexity best: O(1)
        :complexity worst: O(1)
        """
        self.teamCount = n_teams
        self.sites: list[Land] = []


    def add_sites(self, sites: list[Land]) -> None:
        """
        add_sites stores the given sites into self

        :param sites: list of sites to add
        :complexity best: O(n) 
        :complexity worst: O(n)
        :variable n: the length of sites
        """
        for site in sites:
            if site.get_ratio() > 2.5:
                self.sites.append(site)
        print(self.sites)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        simulate_day runs the game logic given the adventurers that the team will have and returns a list of decisions that each team has made (the land chosen and teh amount that was sent to the land)


        :param adventurer_size: the amount of adventurers available to each team
        :return: a list of decisions that each team has made
        :complexity best: 
        :complexity worst:
        """
        self.sites = scoreMergeSort(self.sites, adventurer_size)
        out = []
        for n in range(self.teamCount):
            if len(self.sites) > 0:
                current: Land = self.sites[0]
                if current.get_ratio() > 2.5:
                    guardians = current.get_guardians()
                    treasure = current.get_gold()
                    sending = min(adventurer_size,guardians)
                    current.set_gold(treasure-current.get_reward(sending))
                    current.set_guardians(guardians-sending)
                    if current.get_guardians()==0:
                        self.sites.pop(0)
                    out.append((current, sending))
            else: 
                out.append((None,0))
        return out


