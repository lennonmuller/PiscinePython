def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(m["power"] for m in mages) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 83, 'type': 'weapon'},
        {'name': 'Wind Cloak', 'power': 114, 'type': 'focus'},
        {'name': 'Light Prism', 'power': 78, 'type': 'focus'},
        {'name': 'Light Prism', 'power': 114, 'type': 'focus'}
        ]
    mages = [{'name': 'Jordan', 'power': 68, 'element': 'fire'},
             {'name': 'Nova', 'power': 57, 'element': 'ice'},
             {'name': 'Alex', 'power': 70, 'element': 'light'},
             {'name': 'Ash', 'power': 89, 'element': 'water'},
             {'name': 'Rowan', 'power': 56, 'element': 'earth'}]

    spells = ['heal', 'darkness', 'lightning', 'tsunami']

    print("Artifact sorter:")
    print(artifact_sorter(artifacts))
    print(30*"=")

    print("Power Filter >= 60")
    print(power_filter(mages, 60))
    print(30*"=")

    print("Spell Transformer:")
    print(spell_transformer(spells))
    print(30*"=")

    print("Mage Stats:")
    print(mage_stats(mages))
    print(30*"=")


if __name__ == "__main__":
    main()
