from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack,
                "health": self.health}
        return info

    def play(self, game_state: dict) -> dict:
        if self.is_playable:
            game_state = {"card_played": self.name, "mana_used": self.cost,
                          "effect": "Creature summoned to battlefield"}
        return game_state

    def attack_target(self, target: str) -> dict:
        target_health = 5

        if self.attack > target_health:
            combat = True
        else:
            combat = False

        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": combat}
