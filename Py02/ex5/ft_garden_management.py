class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plants(self, name: str, water: int, sun: int) -> None:
        def is_spaces(spaces: str) -> bool:
            try:
                for sp in spaces:
                    if sp != " ":
                        return False
                return True
            except Exception as e:
                raise PlantError(f"Invalid name {e}")

        if not name or is_spaces(name):
            raise PlantError("Plant name cannot be empty!")
        if water < 1 or water > 10:
            raise PlantError(f"Water level {water} is invalid (1-10)")
        if sun < 2 or sun > 12:
            raise PlantError(f"Sunlight hours {sun} are invalid (2-12)")

        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    if self.plants[plant]["water"] <= 0:
                        raise WaterError("Not enough water in tank")
                    print(f"Watering {plant} - success")
                except GardenError as e:
                    print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' does not exist in garden!")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")

        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    gm = GardenManager()

    plants = [("tomato", 5, 8), ("cactus", 0, 9), ("lettuce", 5, 10)]

    print("\nAdding plants to garden...")
    for name, water, sun in plants:
        try:
            gm.add_plants(name, water, sun)
        except GardenError as e:
            print(f"Error adding plant: {e}")

    try:
        gm.add_plants("    ", 4, 7)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    gm.water_plants()

    print("\nChecking plant health...")
    try:
        gm.check_plant_health("tomato")
    except GardenError as e:
        print(f"Error checking tomato: {e}")

    try:
        gm.check_plant_health("lettuce")
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
