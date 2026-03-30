class AggressiveStrategy:
    def __init__(self, current_mana):
        self.current_mana = current_mana
        self.mana_needed = 5

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if self.current_mana < self.mana_needed:
            raise ValueError("Not enough mana to execute strategy")
        else:
            try:
                names = []
                damage = 0

                for item in hand:
                    split = item.split('(')
                    names.append(split[0].strip())
                    damage += int(split[1].strip(')'))

                return {'cards_played': names,
                        'mana_used': self.mana_needed,
                        'targets_attacked': battlefield,
                        'damage_dealt': damage}
            except ValueError:
                print("Invalid data format. Use: '"
                      "['card_name (power: int)', ...]")

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
