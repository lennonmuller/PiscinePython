from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    hand_played = ["Fire Dragon (5)", "Goblin Warrior (0)",
                   "Lightning Bolt (3)"]

    battlefield = ['Enemy Player']

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy(9)

    game_engine = GameEngine(hand_played, battlefield)

    game_engine.configure_engine(factory, strategy)
    print(f"Factory: {game_engine.factory.__class__.__name__}")

    print(f"Strategy: {strategy.get_strategy_name()}")

    fantasy_deck = FantasyCardFactory()
    print(f"Available types: {fantasy_deck.get_supported_types()}\n")

    print("Simulating aggressive turn...")

    print(f"Hand: {hand_played}\n")

    print("Turn execution:")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print("Actions: "
          f"{game_engine.simulate_turn()}")

    print(f"\nGame Report: {game_engine.get_engine_status()}")

    print("\nAbstract Factory + Strategy Pattern: Maximum "
          "flexibility achieved!")


if __name__ == "__main__":
    main()
