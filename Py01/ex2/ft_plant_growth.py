class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount) -> None:
        self.height += amount

    def age_plant(self, days) -> None:
        self.age += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        ]

    print("=== Day 1 ===")
    print(garden[0].get_info())
    initial_height = garden[0].height

    for day in range(6):
        garden[0].grow(1)
        garden[0].age_plant(1)

    print("=== Day 7 ===")
    print(garden[0].get_info())

    final_height = garden[0].height - initial_height
    print(f"Growth this week: +{final_height}cm")
