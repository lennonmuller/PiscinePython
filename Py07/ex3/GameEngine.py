from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, hand: list, battlefield: list) -> None:
        self.strategy = None
        self.factory = None
        self.turns = 0
        self.battlefield = battlefield
        self.total_damage = 0
        self.hand = hand

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turns += 1
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage = result.get('damage_dealt')
        return result

    def get_engine_status(self) -> dict:
        return {'turns_simulated': self.turns,
                'strategy_used': self.strategy.get_strategy_name(),
                'total_damage': self.total_damage,
                'cards_created': len(self.hand)}
