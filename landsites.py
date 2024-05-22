from dataclasses import dataclass
from data_structures.referential_array import ArrayR
from random_gen import RandomGen
from data_structures.heap import *

# Land sites can have names other than the list follows.
# This is just used for random generation.
LAND_NAMES = [
    "Dawn Island",
    "Shimotsuki Village",
    "Gecko Islands",
    "Baratie",
    "Conomi Islands",
    "Drum Island",
    "Water 7"
    "Ohara",
    "Thriller Bark",
    "Fish-Man Island",
    "Zou",
    "Wano Country",
    "Arabasta Kingdom",
    # 13 🌞 🏃‍♀️
    "Loguetown",
    "Cactus Island",
    "Little Garden",
    "Jaya",
    "Skypeia",
    "Long Ring Long Land",
    "Enies Lobby",
    "Sabaody Archipelago",
    "Impel Down",
    "Marineford",
    "Punk Hazard",
    "Dressrosa",
    "Whole Cake Island",
    "Ys Island",
]


@dataclass
class Land:

    name: str
    gold: float
    guardians: int

    @classmethod
    def random(cls):
        return Land(
            RandomGen.random_choice(LAND_NAMES),
            RandomGen.randint(0, 500),
            RandomGen.randint(0, 300),
        )

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> float:
        return self.gold

    def get_guardians(self) -> int:
        return self.guardians

    def set_gold(self, new_gold: float) -> None:
        self.gold = new_gold

    def set_guardians(self, new_guardians: int) -> None:
        self.guardians = new_guardians

    def get_ratio(self):
        # return self.guardians/(self.gold+1)
        return self.gold/(self.guardians+1)
        
    def get_reward(self, adventurers):
        return min(((adventurers*self.get_gold())/self.get_guardians()),self.get_gold())
    
    def get_score(self, available):
        sent=min(available,self.get_guardians())
        return 2.5*(available-sent) + self.get_reward(sent)
    
    def ge_score(self,other,available):
        return self.get_score(available) >= other.get_score(available)
    
    def lt_score(self,other,available):
        return self.get_score(available) < other.get_score(available)

    def __lt__(self, other):
        return self.get_ratio() < other.get_ratio()    
    
    def __gt__(self, other):
        return self.get_ratio() > other.get_ratio()    
    
    def __le__(self, other):
        return self.get_ratio() <= other.get_ratio() 
       
    def __ge__(self, other):
        return self.get_ratio() >= other.get_ratio()
    





class ScoreHeap(MaxHeap):
    def __init__(self, max_size: int, adventurers) -> None:
        self.length = 0
        self.the_array = [None] * max_size
        self.adventurers = adventurers

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length
        """
        item = self.the_array[k]
        while k > 1 and item.get_score(self.adventurers) > self.the_array[k // 2].get_score(self.adventurers):
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item
        

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.
        :pre: 1 <= k <= self.length // 2
        """

        if 2 * k == self.length or self.the_array[2 * k].get_score(self.adventurers) > self.the_array[2 * k + 1].get_score(self.adventurers):
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            :pre: 1 <= k <= self.length
            :complexity: ???
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child].get_score(self.adventurers) <= item.get_score(self.adventurers):
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

    def get_max(self) -> T:
        """ Remove (and return) the maximum element from the heap. """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt

    @classmethod
    def heapify(cls, points: ArrayR[T], adventurers):
        self = ScoreHeap((2 * len(points) + 2),adventurers)
        self.length = len(points)
        for i in range(len(points)):
            self.the_array[i+1] = points[i]
        for k in range(len(points), 0, -1):
            self.sink(k)
        return self
