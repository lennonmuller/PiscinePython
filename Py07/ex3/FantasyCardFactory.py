from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


class FantasyCardFactory:
    def __init__(self):
        self.types = {'creatures': ['dragon', 'goblin'],
                      'spells': ['fireball'],
                      'artifacts': ['mana_ring']}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(str, name_or_power):
            if name_or_power == 'dragon':
                return CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
            elif name_or_power == 'goblin':
                return CreatureCard('Goblin Warrior', 2, 'Common', 1, 1)
            else:
                raise ValueError(f"this {name_or_power} is not a valid "
                                 "creature")

        elif isinstance(int, name_or_power):
            if name_or_power == 1:
                return CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
            elif name_or_power == 2:
                return CreatureCard('Goblin Warrior', 2, 'Common', 1, 1)
            else:
                raise ValueError("Invalid creature reference: no creature is "
                                 "associated with the given number.")

        else:
            return None

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(str, name_or_power):
            if name_or_power == 'fireball':
                return SpellCard("Fireball", 3, "Common", "damage")
            elif name_or_power == 'lightning':
                return SpellCard("Lightning Bolt", 3, "Common", "damage")
            else:
                raise ValueError(f"this {name_or_power} is not a valid"
                                 "spell")

        elif isinstance(int, name_or_power):
            if name_or_power == 1:
                return SpellCard("Fireball", 3, "Common", "damage")
            if name_or_power == 2:
                return SpellCard("Lightning Bolt", 3, "Common", "damage")
            else:
                raise ValueError("Invalid spell reference: no spell is "
                                 "associated with the given number.")
        else:
            return None

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(str, name_or_power):
            if name_or_power == 'mana_ring':
                return ArtifactCard("Mana Ring", 2, "Common", 5,
                                    "Permanent: +1 mana per turn")
            else:
                raise ValueError(f"this {name_or_power} is not a valid"
                                 "artifact")

        elif isinstance(int, name_or_power):
            if name_or_power == 1:
                return ArtifactCard("Mana Ring", 2, "Common", 5,
                                    "Permanent: +1 mana per turn")
            else:
                raise ValueError("Invalid artifact reference: no artifact is "
                                 "associated with the given number.")
        else:
            return None

    def create_themed_deck(self, size: int) -> dict:
        deck = Deck()

        number_types = 3
        per_type = round(size / number_types)

        for _ in range(per_type):
            deck.add_card(self.create_creature('dragon'))
            deck.add_card(self.create_creature('goblin'))

        for _ in range(per_type):
            deck.add_card(self.create_spell('fireball'))

        for _ in range(per_type):
            deck.add_card(self.create_artifact('mana_ring'))

        return deck.get_deck_stats()

    def get_supported_types(self) -> dict:
        return self.types
