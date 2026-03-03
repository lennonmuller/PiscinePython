class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return f"{self.name} (Flower): {super().get_info()}"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_info(self) -> str:
        return f"{self.name} (Tree): {super().get_info()}"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutricional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutricional_value

    def describe(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        return f"{self.name} (Vegetable): {super().get_info()}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 50, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    brocoli = Vegetable("Brocoli", 30, 60, "spring harvest", "vitamin B6")

    print(f"{rose.get_info()}, {rose.color} color")
    rose.bloom()
    print()
    print(f"{oak.get_info()}, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()
    print(f"{brocoli.get_info()}, {brocoli.harvest_season}")
    tomato.describe()
