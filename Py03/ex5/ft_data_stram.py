from typing import Generator


def game_generate(total_events: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie", "diana", "zimbzbwe", "bob_marley",
               "ratazana2000", "fantasmao", "nivi_jr", "gabigo"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for _ in range(1000):
        