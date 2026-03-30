from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 defense_damage: int, id, rating) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense_damage)
        self.id = id
        self.rating = rating
        self.total_wins = 0
        self.total_losses = 0

    def play(self, game_state: dict) -> dict:
        game_state = {"card_played": self.name, "mana_used": self.cost,
                      "effect": "3 Damage"}
        return game_state

    def attack(self, target) -> dict:
        combat_type = "melee"
        return {"attacker": self.name, "target": target,
                "damage": self.damage, "combat_type": combat_type}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = round((incoming_damage / 3))

        still_alive = False

        if damage_taken < self.cost:
            still_alive = True

        return {"defender": self.name, "damage_taken": damage_taken,
                "damage_defended": self.defense_damage,
                "still_alive": still_alive}

    def calculate_rating(self) -> int:
        return self.rating + (self.total_wins * 16) - (self.total_losses * 16)

    def update_wins(self, wins: int) -> None:
        self.total_wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.total_losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.total_wins}-{self.total_losses}"
        }

    def get_combat_stats(self) -> dict:
        return {'damage': self.damage,
                'defense_damage': self.defense_damage}

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.total_wins,
            "losses": self.total_losses
        }
