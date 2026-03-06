def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    def is_spaces(spaces: str) -> bool:
        try:
            for sp in spaces:
                if sp != ' ':
                    return False
            return True
        except Exception as e:
            raise ValueError(f"Invalid name {e}")
    if not plant_name or is_spaces(plant_name):
        raise ValueError("Plant name cannot be empty!")

    if water_level < 0:
        raise ValueError("Water level cannot be negative")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 0:
        raise ValueError("Sunlight hours cannot be negative")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 1))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
