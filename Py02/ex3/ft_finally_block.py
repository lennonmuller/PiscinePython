def water_plants(plant_list: list[str]) -> bool:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    normal = water_plants(["tomato", "lettuce", "carrots"])
    if normal:
        print("Watering completed successfully!")
    else:
        print("\nCleanup always happens, even with errors")

    print("\nTesting with error...")
    normal = water_plants(["tomato", None])
    if normal:
        print("Watering completed successfully!")
    else:
        print("\nCleanup always happens, even with errors")


if __name__ == "__main__":
    test_watering_system()
