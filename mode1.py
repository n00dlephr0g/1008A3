from landsites import Land
from data_structures.bst import BinarySearchTree
from algorithms.mergesort import mergesort

class Mode1Navigator:
    """
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
        # self.sites = BinarySearchTree()
        # for land in sites:
        #     self.sites[land.get_ratio()] = land


    def select_sites(self) -> list[tuple[Land, int]]:
        """
        select_sites generate and optimises a list of sites to invade and the amount of adventurers to send to each site

        :return: a list of tuples that contains the site and the corresponding adventurer count
        :complexity best: 
        :complexity worst:
        
        """
        remaining : int = int(self.adventurers) #making sure im not editing the instance field
        n = 0
        output=[]
        while remaining > 0: #n
            try:
                currentLand = self.sites[n]
            except IndexError:
                break
            n+=1
            amountToSend = min(currentLand.get_guardians(), remaining) # 1
            remaining -= amountToSend
            tup = (currentLand, amountToSend)
            output.append(tup) # 1
        return output
                
    
    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        select_sites_from_adventure_numbers _summary_

        :param adventure_numbers: _description_
        :raises NotImplementedError: _description_
        :return: _description_
        :complexity best: 
        :complexity worst:
        """
        raise NotImplementedError()

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
