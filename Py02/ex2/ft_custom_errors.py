class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def cause_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def cause_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        cause_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        cause_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting chatching all garden errors...")
    for errors in (cause_plant_error, cause_water_error):
        try:
            errors()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
