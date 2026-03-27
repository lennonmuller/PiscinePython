from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, defense_damage: int, mana_cost: int,
                 spell_power: int) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense_damage)
        Magical.__init__(self, mana_cost, spell_power)

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

    def get_combat_stats(self) -> dict:
        return {"damage": self.damage,
                "defense_damage": self.defense_damage}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        total_mana = 7

        total_mana -= self.mana_cost
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": self.mana_cost}, total_mana

    def channel_mana(self, amount: int) -> dict:
        return {"channeled": self.spell_power, "total_mana": amount}

    def get_magic_stats(self) -> dict:
        return {"spell_power": self.spell_power, "cost": self.mana_cost}
