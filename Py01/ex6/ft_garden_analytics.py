class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, amount: int) -> None:
        self.height += amount
        self.total_growth += amount
        print(f"{self.name} grew {amount}cm")

    def score(self) -> int:
        return self.height

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points = points

    def score(self) -> int:
        return self.height + self.points

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.points}"
        )


class GardenManager:
    total_gardens = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, amount: int) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)

    def garden_score(self) -> int:
        return sum(plant.score() for plant in self.plants)

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())

        stats = self.GardenStats(self.plants)

        print(
            f"\nPlants added: {stats.count_plants()}, "
            f"Total growth: {stats.total_growth()}cm"
        )

        regular, flowering, prize = stats.type_count()

        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls):
        alice = cls("Alice")
        bob = cls("Bob")
        return alice, bob

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    class GardenStats:
        def __init__(self, plants: list[Plant]) -> None:
            self.plants = plants

        def count_plants(self) -> int:
            return len(self.plants)

        def total_growth(self) -> int:
            return sum(
                plant.total_growth for plant in self.plants
            )

        def type_count(self):
            regular = flowering = prize = 0

            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice, bob = GardenManager.create_garden_network()

    # Alice garden
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all(1)
    alice.report()

    # Bob garden
    cactus = Plant("Cactus", 40)
    daisy = PrizeFlower("Daisy", 30, "white", 5)

    bob.add_plant(cactus)
    bob.add_plant(daisy)

    bob.grow_all(9)
    bob.report()

    print(
        f"\nGarden scores - Alice: {alice.garden_score()}, "
        f"Bob: {bob.garden_score()}"
    )

    print(
        f"Height validation test: "
        f"{GardenManager.validate_height(10)}"
    )

    print(
        f"Total gardens managed: "
        f"{GardenManager.total_gardens}"
    )
