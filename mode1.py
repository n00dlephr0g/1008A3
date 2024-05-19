from landsites import Land
from data_structures.bst import BinarySearchTree
from algorithms.mergesort import mergesort

class Mode1Navigator:
    """
    Mode1Navigator class

    instance variables
        sites
            a python list containing the Land objects that the Mode1Navigator has access to.
            this list is sorted at the start based on the gold to guardian ratio.
            the choice to keep the sites attribute as a sorted python list instead of using other
            data structures is due to its ease of use and the simplicity of list data structures.

        adventurers
            an integer of how many adventurers the Mode1Navigator has to its disposal.
            can change over time.

        length:
            an integer of how many lands are in the list.
            is instanciated for convenience in 2 of the methods.

    methods
        __init__()
            initialises instance variables.
            also sorts the sites list using mergesort provided before storing it.
            the mergesort makes the constructor have a TC of O(n*log(n))
            where n is the size of the provided sites list

        select_sites()
            returns the optimal list of sites to invade and amount of adventurers to send to each.
            total amount of adventurers to send does not exceed the amount of adventurers on hand.
            since the sites variable was already sorted in the init method, this function goes 
            through each Land objects in optimal order until there will be no troops left to send.
            doesnt actually modify any objects in self.sites or change the value of self.adventurers.
            the loop included makes this method have a TC of O(n)
            where n is the length of the sites list

        select_sites_from_adventure_numbers()
            returns a list of maximum rewards that can be reached given a list of adventurer counts.
            uses a similar loop as select_sites() but calls that loop for every different adventurer
            count. this means the logic includes 2 loops, one for inputs and one for sites.
            these loops brings the complexity to O(n*m)
            where n is the length of sites
            where m is the length of inputs

        update_sites()
            updates a Land object
            nothing special, just uses Land.set_guardians() and Land.set_gold() to update the object.

    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306

    
    
    """
    
    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        __init__ constructor for mode 1 navigator class

        :param sites: a list of Land objects that this instance should have access to
        :param adventurers: an integer amount of adventurers that this instance will have access to
        :complexity best: O(n*log(n)) occurs no matter what
        :complexity worst: O(n*log(n)) occurs no matter what
        :variable n: the lenght of parameter sites
        """
        self.adventurers: int = adventurers
        self.sites = mergesort(sites)
        self.length = len(self.sites)
        # self.sites = BinarySearchTree()
        # for land in sites:
        #     self.sites[land.get_ratio()] = land


    def select_sites(self) -> list[tuple[Land, int]]:
        """
        select_sites generate and optimises a list of sites to invade and the amount of adventurers to send to each site

        :return: a list of tuples that contains the site and the corresponding adventurer count
        :complexity best: O(1) occurs if there are no adventurers left or there are no sites
        :complexity worst: O(n) occurs if there are more than one site and there are adventurers
        :variable n: amount of sites
        """
        output=[]
        remaining : int = int(self.adventurers) # defensive copying
        for n in range(self.length):
            n <= self.length
            currentLand = self.sites[n]
            amountToSend = min(currentLand.get_guardians(), remaining) # 1
            remaining -= amountToSend
            tup = (currentLand, amountToSend)
            output.append(tup) # 1
        return output
                
    
    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        select_sites_from_adventure_numbers calculates the maximum amount of reward you can make with different adventurer numbers

        :param adventure_numbers: list of integer counts of adventurers
        :return: returns corresponding reward in the same order of inputs
        :complexity best: O(m) 
        :complexity worst: O(m*n)
        :variable n: amount of sites
        :variable m: size of adventure_numbers
        """
        output = []
        for adventurers in adventure_numbers:
            currentReward = 0
            for n in range(self.length):
                currentLand = self.sites[n]
                amountToSend = min(currentLand.get_guardians(), adventurers)
                adventurers -= amountToSend
                currentReward += currentLand.get_reward(amountToSend)
            output.append(currentReward)
        return output


    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        update_site udpates specified lan

        :param land: target land
        :param new_reward: target reward
        :param new_guardians: target guardians
        :complexity best: O(1) occurs no matter what
        :complexity worst: O(1) occurs no matter what
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
        return
