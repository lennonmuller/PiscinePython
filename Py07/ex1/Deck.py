from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
import random


class Deck:
    def __init__(self) -> None:
        self.card_list = []

    def add_card(self, card: Card) -> None:
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        if len(self.card_list) > 1:
            random.shuffle(self.card_list)
        else:
            print("Deck is too small to shuffle")

    def draw_card(self) -> Card:
        return self.card_list.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.card_list)
        total_cost = sum(card.cost for card in self.card_list)
        average = (round(total_cost / total_cards, 1)
                   if total_cards > 0 else 0)

        info = {"total_cards": len(self.card_list),
                "creatures": (sum(isinstance(card, CreatureCard)
                                  for card in self.card_list)),
                "spells": (sum(isinstance(card, SpellCard)
                               for card in self.card_list)),
                "artifacts": (sum(isinstance(card, ArtifactCard)
                                  for card in self.card_list)),
                "avg_cost": (average)}

        return info
