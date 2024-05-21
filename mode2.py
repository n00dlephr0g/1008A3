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
            if site.get_ratio() < 2/5:
                self.sites.append(site)
        print(self.sites)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = mergesort(self.sites)
        out = []
        for n in range(self.teamCount):
            pass


def scoremergesort(sites: list[Land], total, sent):
    if len(sites) <= 1:
        return sites
    break_index = (len(sites)+1) // 2
    l1 = scoremergesort(sites[:break_index], total, sent)
    l2 = scoremergesort(sites[break_index:], total, sent)
    return scoremerge(l1, l2, total, sent)
    


def scoremerge(l1: list[Land], l2: list[Land], total, sent):
    new_list: list[Land] = []
    cur_left = 0
    cur_right = 0
    while cur_left < len(l1) and cur_right < len(l2):
        if l1[cur_left].score(total, sent) >= l2[cur_right].score(total, sent):
            new_list.append(l1[cur_left])
            cur_left += 1
        else:
            new_list.append(l2[cur_right])
            cur_right += 1
    new_list += l1[cur_left:]
    new_list += l2[cur_right:]
    return new_list

