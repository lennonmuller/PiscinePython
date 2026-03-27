from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from .EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    Card_methods = [method for method in dir(Card)
                    if not method.startswith("__")
                    and callable(getattr(Card, method))]

    Combatable_methods = [method for method in dir(Combatable)
                          if not method.startswith("__")
                          and callable(getattr(Combatable, method))]

    Magical_methods = [method for method in dir(Magical)
                       if not method.startswith("__")
                       and callable(getattr(Magical, method))]

    print("EliteCard capabilities:")
    print(f"- Card: {Card_methods}")
    print(f"- Combatable: {Combatable_methods}")
    print(f"- Magical: {Magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    arcane_warrior = EliteCard("Arcane Warrior", 3, "Legendary", 5, 3, 4, 3)

    print("\nCombate phase:")

    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic phase:")

    info, amount = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])

    print(f"Spell cast: {info}")
    print(f"Mana channel: {arcane_warrior.channel_mana(amount)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
