def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        plants = {"Aguacate": 5, "Pastel De Letche": 3}
        plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        int("abc")
        10 / 0
    except Exception:
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    garden_operations()

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
