from .TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id] = card

        return (
            f"{card.name} (ID: {card.id}):\n"
            "- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.total_wins}-{card.total_losses}\n"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner, loser = random.sample([card1, card2], 2)

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        list_cards = sorted(self.cards.values(), key=lambda i: i.rating,
                            reverse=True)
        return list_cards

    def generate_tournament_report(self) -> dict:
        ratings = [card.rating for card in self.cards.values()]

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": round(sum(ratings) / len(ratings)),
            "platform_status": "active"
        }
