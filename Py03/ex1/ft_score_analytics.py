import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]

    if len(args) == 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics <score1> "
            "<score2> ..."
        )
        return

    scores = []

    for arg in args:
        try:
            value = int(arg)
            scores.append(value)
        except ValueError:
            print(f"Invalid score: {arg}")

    if len(scores) == 0:
        print("No valid scores were provided.")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average = total_score / total_players
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    score_analytics()
