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
    available: int = 0

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

    def get_ratio(self):
        return self.gold/(self.guardians+1)
        
    def get_inverse(self):
        return self.guardians/(self.gold+1)

    def get_reward(self, adventurers):
        return round(min(((adventurers*self.get_gold())/(self.get_guardians()+0.0000001)),self.get_gold()))

    def get_score(self):
        sent=min(self.available,self.get_guardians())
        return 2.5*(self.available-sent) + self.get_reward(sent)

    def set_gold(self, new_gold: float) -> None:
        self.gold = new_gold

    def set_guardians(self, new_guardians: int) -> None:
        self.guardians = new_guardians
    
    def set_available(self, available):
        self.available = available


    def __lt__(self, other):
        return self.get_score() < other.get_score()    
    
    def __gt__(self, other):
        return self.get_score() > other.get_score()    
    
    def __le__(self, other):
        return self.get_score() <= other.get_score() 
       
    def __ge__(self, other):
        return self.get_score() >= other.get_score()
    
