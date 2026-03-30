from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n===  DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    tournament = TournamentPlatform()

    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 5, 2,
                                 "dragon_001", 1200)
    ice_wizard = TournamentCard("Ice Wizard", 3, "Rare", 3, 2,
                                "wizard_001", 1150)

    print(tournament.register_card(fire_dragon))
    print(tournament.register_card(ice_wizard))

    print("Creating tournament match...")

    match = tournament.create_match('dragon_001', 'wizard_001')
    print(f"Match result: {match}")

    print("\nTournament Leaderboard:")
    for n, card in enumerate(tournament.get_leaderboard(), start=1):
        info = card.get_rank_info()

        print(f"{n}. {card.name} - Rating: {int(info['rating'])}"
              f"({info['record']})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===\n"
          "All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
