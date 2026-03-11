def analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players = ["alice", "bob", "charlie", "diana", "juninho_cancelado"]
    scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 1300,
              "juninho_cancelado": 5000}
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "treasure_hunter",
                  "arena_champion"],
        "bob": ["first_kill", "level_5"],
        "charlie": ["first_kill", "level_10", "dungeon_master"],
        "diana": ["first_kill", "level_10", "boss_slayer", "speed_runner"],
        "juninho_cancelado": ["first_kill", "level_10", "cancelado"]
    }

    high_scores = [p for p in players if scores[p] > 2000]
    doubled_scores = [scores[p] * 2 for p in players]

    print("=== List Comprehension Example ===")
    print("High scores (>2000):", high_scores)
    print("Scores doubled:", doubled_scores)
    print("Active players:", players)

    score_map = {p: scores[p] for p in players}

    score_categories = {
        "high": len([p for p in players if scores[p] >= 2000]),
        "medium": len([p for p in players if 1500 <= scores[p] < 2000]),
        "low": len([p for p in players if scores[p] < 1500])
    }

    achievement_count = {p: len(achievements[p]) for p in players}

    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", score_map)
    print("Score categories:", score_categories)
    print("Achievements per player:", achievement_count)

    unique_achievements = {ach for plist in achievements.values()
                           for ach in plist}

    print("\n=== Set Comprehension Examples ===")
    print("Unique achievements:", unique_achievements)

    total_players = len(players)
    total_uniq_achiv = len(unique_achievements)
    average_score = sum(scores.values()) / len(scores)

    top_player = max(scores, key=lambda p: scores[p])
    top_score = scores[top_player]
    top_achievements = len(achievements[top_player])

    print("\n=== Combined Analysis ===")
    print("total players:", total_players)
    print("Total unique achievements:", total_uniq_achiv)
    print("Average score:", average_score)
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_achievements} achievements)")


if __name__ == "__main__":
    analytics_dashboard()
