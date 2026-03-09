from typing import Generator
import random


def game_generate(total_events: int) -> Generator[str, None, int]:
    players = ["alice", "bob", "charlie", "diana", "zimbzbwe", "bob_marley",
               "ratazana2000", "fantasmao", "nini_jr", "gabigo"]
    actions = ["killed monster", "found treasure", "leveled up"]

    player_levels = {player: 1 for player in players}
    

    for _ in range(total_events):
        player = random.choice(players)
        action = random.choice(actions)
        if action == "leveled up":
            player_levels[player] += 1
        level_atual = player_levels[player]
        yield f"Player {player} (level {level_atual}) {action}"


def stream_analytics() -> None:
    print("=== Game Data Stream Processor ===\n")

    qty = 1000
    print(f"Processing {qty} game events...\n")
    i = 1
    for event in game_generate(qty):
        print(f"Event {i}: {event}")
        i += 1

    for players in game_generate(qty):
        if 


    print(f"\n=== Stream Analytics ===")
    print(f"Total events processed: {qty}")
    print(f"High-level players (10+): {lvl}")

if __name__ == "__main__":
    stream_analytics()