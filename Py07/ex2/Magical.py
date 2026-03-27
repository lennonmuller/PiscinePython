from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self, mana_cost: int, spell_power: int) -> None:
        self.mana_cost = mana_cost
        self.spell_power = spell_power

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
