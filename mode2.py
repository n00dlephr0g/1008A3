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
            if site.get_ratio() > 2.5:
                self.sites.append(site)
        print(self.sites)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
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


