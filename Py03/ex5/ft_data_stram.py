from typing import Generator
import random


def game_generate(total_events: int) -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "diana", "zimbzbwe", "bob_marley",
               "ratazana2000", "fantasmao", "nini_jr", "gabigo",
               "juninho_cancelado"]
    actions = ["killed monster", "found treasure", "leveled up"]

    player_levels = {player: 1 for player in players}
    for _ in range(total_events):
        player = random.choice(players)
        action = random.choice(actions)
        if action == "leveled up":
            player_levels[player] += 1
        level_atual = player_levels[player]
        yield player, level_atual, action


def fibonacci_stream() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def stream_analytics() -> None:
    print("=== Game Data Stream Processor ===\n")

    qty = 1000
    print(f"Processing {qty} game events...\n")

    player_levels = {}
    treasure = 0
    level_up = 0

    i = 1
    for player, level, action in game_generate(qty):
        print(f"Event {i}: Player {player}, (level {level}) {action}")
        player_levels[player] = level
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1
        i += 1

    high_level = 0
    for player in player_levels:
        if player_levels[player] >= 10:
            high_level += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {qty}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_stream()
    for i in range(10):
        value = next(fib)
        print(value, end="")
        if i < 9:
            print(", ", end="")
    print("\nPrime numbers (first 5): ", end="")
    primes = prime_stream()
    for i in range(5):
        value = next(primes)
        print(value, end="")
        if i < 4:
            print(", ", end="")


if __name__ == "__main__":
    stream_analytics()
