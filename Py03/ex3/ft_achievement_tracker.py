def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer",
                   "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}")

    print("\n=== Archievements Analytics ===\n")
    all_unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    all_common = alice.intersection(bob).intersection(charlie)
    print(f"\nCommon to all players: {all_common}")
    rare = (
        (alice - bob - charlie)
        .union(bob - alice - charlie)
        .union(charlie - alice - bob)
    )
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    achievement_tracker()
