from landsites import *
from algorithms.mergesort import *

class Mode2Navigator:
    """
    Mode2Navigator class

    instance variables
        teamCount
            integer amount of teams participating in the game
        
        sites
            a list of Land objects that the participants have access to

    methods
        __init__()
            constructor method that initialises self.sites as an empty list
            and initiates self.teamCount based on parameter

        add_sites()
            takes a list of sites that are to be added and adds them if
            the island has a ratio of more than 2.5 (this is the threshold
            for which islands will start benefitting from sending troops)

        simulate_day()
            runs the game logic given the adventurers that the team will have 
            on the day and returns a list of decisions that each team has 
            made (the land chosen and the amount that was sent to the land).
            this method achieves a best-worst time complexity of O(n +k*log(n))
            where n are the sites available and k is the team size by 
            utilising the heap data structure to organise self.site before
            conducting the game logic.


    """

    def __init__(self, n_teams: int) -> None:
        """
        __init__ initialises a game given a number of teams

        :param n_teams: an integer amount of teams
        :complexity best: O(1) occurs all the time
        :complexity worst: O(1) occurs all the time
        """
        self.teamCount = n_teams
        self.sites: list[Land] = []


    def add_sites(self, sites: list[Land]) -> None:
        """
        add_sites stores the given sites into self

        :param sites: list of sites to add
        :complexity best: O(n) occurs all the time
        :complexity worst: O(n) occurs all the time
        :variable n: the length of sites
        """
        for site in sites: # O(n)
            if site.get_ratio() > (5/2):
                self.sites.append(site) # O(1)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        simulate_day runs the game logic given the adventurers that the team will have and returns a list of decisions that each team has made (the land chosen and the amount that was sent to the land)

        :param adventurer_size: the amount of adventurers available to each team
        :return: a list of decisions that each team has made
        :complexity best: O(n + k*log(n)) occurs all the time
        :complexity worst: O(n + k*log(n)) occurs all the time
        :variable n: length of self.sites
        :variable k: the magnitude of self.teamCount
        """
        for site in self.sites: # O(n)
            site.set_available(adventurer_size)
        sites: MaxHeap = MaxHeap.heapify(self.sites) #O(log(n))
        out = []
        for k in range(self.teamCount): #O(k)
            if len(sites) > 0:
                current: Land = sites.get_max() # O(log(n))
                guardians = current.get_guardians()
                treasure = current.get_gold()
                sending = min(adventurer_size,guardians)
                current.set_gold(treasure-current.get_reward(sending))
                current.set_guardians(guardians-sending)
                out.append((current, sending))
                if current.get_guardians() > 0:
                    sites.add(current)
            else: 
                out.append((None,0))
        return out


