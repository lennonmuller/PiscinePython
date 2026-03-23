from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity}
        return info

    def is_playable(self, available_mana: int) -> bool:
        try:
            return self.cost <= available_mana
        except ValueError:
            print("Error: available mana must be an integer")
