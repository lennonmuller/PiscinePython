def analytics_dashboard() -> None:
    players = [
        {'name': 'alice',
         'status': 'active',
         'region': 'north',
         'score': 2300,
         'achievements': ['first_kill', 'level_10', 'boss_slayer',
                          'boss_slayer', 'boss_slayer']},
        {'name': 'bob',
         'status': 'active',
         'region': 'east',
         'score': 1800,
         'achievements': ['first_kill', 'level_10',
                          'boss_slayer']},
        {'name': 'charlie',
         'status': 'active',
         'region': 'central',
         'score': 2150,
         'achievements': ['first_kill', 'level_10', 'boss_slayer',
                          'boss_slayer']},
        {'name': 'diana',
         'status': 'inactive',
         'region': 'north',
         'score': 2050,
         'achievements': ['first_kill', 'level_10',
                          'boss_slayer', 'boss_slayer']},
        {'name': 'juninho_cancelado',
         'status': 'active',
         'region': 'north',
         'score': 5000,
         'achievements': ['first_kill', 'level_10',
                          'boss_slayer', 'cancelado', 'cancelado']}
    ]

    high_scores = [p['name'] for p in players if p['score'] > 2000]
    scores_doubled = [p['score'] * 2 for p in players]
    active_players = [p['name'] for p in players if p['status'] == 'active']

    player_scores = {p['name']: p['score'] for p in players
                     if p['status'] == 'active'}
    score_categories = {"high": 3, "medium": 2, "low": 1}
    achievement_counts = {p['name']: len(p['achievements']) for p in players
                          if p['status'] == 'active'}

    unique_players = {p['name'] for p in players}
    unique_achievements = {achievement for p in players
                           for achievement in p['achievements']}
    active_regions = {p['region'] for p in players}

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(p['score'] for p in players) / total_players
    top_p = max(players, key=lambda p: p['score'])

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_p['name']} ({top_p['score']} points, "
          f"{len(top_p['achievements'])} achievements)")


if __name__ == "__main__":
    analytics_dashboard()
