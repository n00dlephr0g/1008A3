from landsites import Land
from data_structures.bst import BinarySearchTree


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    
    """
    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.adventurers: int = adventurers
        self.sites = BinarySearchTree()
        for land in sites:
            ratio: float = land.get_gold()/(land.get_guardians()+1)
            self.sites[ratio] = land

    def bound_max(self,bound):
        current = self.sites.root
        while True:
            if current.right == bound:
                return current
            else:
                return

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        remaining : int = int(self.adventurers) #making sure im not editing the instance field
        output=[]
        bound=None
        while remaining > 1:
            current=self.bound_max(bound)
            currentLand:Land = current.item
            currentGuardians = currentLand.get_guardians()
            amountToSend = min(remaining, currentGuardians)
            remaining -= amountToSend
            tup = (currentLand, amountToSend)
            output.append(tup)
            bound = current
        return output
                


    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        update_site udpates specified lan

        :param land: target land
        :param new_reward: target reward
        :param new_guardians: target guardians
        best case and worst case:
        O(1)
        occurs constantly
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
        return
