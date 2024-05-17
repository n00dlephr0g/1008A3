from dataclasses import dataclass
from random_gen import RandomGen

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
        return self.guardians/(self.gold+1)
        # return self.gold/(self.guardians+1)

    def get_reward(self, adventurers):
        return min(((adventurers*self.get_gold())/self.get_guardians()),self.get_gold())
    
    def __lt__(self, other):
        return self.get_ratio() < other.get_ratio()    
    
    def __gt__(self, other):
        return self.get_ratio() > other.get_ratio()    
    
    def __le__(self, other):
        return self.get_ratio() <= other.get_ratio() 
       
    def __ge__(self, other):
        return self.get_ratio() >= other.get_ratio()