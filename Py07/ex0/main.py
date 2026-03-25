from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreature Info:")
    info = fire_dragon.get_card_info()
    print(f"{info}\n")

    mana = 6
    print(f"Playing {fire_dragon.name} with {mana} mana availeble")

    is_playable = fire_dragon.is_playable(mana)
    print(f"Playable: {is_playable}")

    game_state = {"is_playable": is_playable}
    if is_playable:
        print('Play result: '
              f'{fire_dragon.play(game_state)}')

        target = "Globin Warrior"
        print(f"\n{fire_dragon.name} attacks {target}:")
        print(f"Attack result: {fire_dragon.attack_target(target)}")
        mana = mana - fire_dragon.cost

    print(f"\nTesting insuficcient mana ({mana} available): ")

    is_playable = fire_dragon.is_playable(mana)
    print(f"Playable: {is_playable}")

    if is_playable:
        print('Play result: '
              f'{fire_dragon.play({game_state})}')
        target = "Globin Warrior"
        print(f"\n{fire_dragon.name} attacks {target}:")
        print(f"Attack result: {fire_dragon.attack_target(target)}")
        mana = mana - fire_dragon.cost
    else:
        print("Insuficcient mana")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
