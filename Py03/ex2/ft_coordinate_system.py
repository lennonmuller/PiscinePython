import math


def parse_coordinates(coordinates: str) -> tuple[int, int, int]:
    parts = coordinates.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinate must have exactly 3 values")

    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except Exception as e:
        raise e


def distance_3d(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    pos = (10, 20, 5)
    print(f"\nPosition created {pos}")

    origin = (0, 0, 0)
    dist = distance_3d(origin, pos)
    print(f"Distance between {origin} and {pos}: {dist:.2f}")

    coordinate = "3,4,0"
    print(f"\nParsing coordinates: {coordinate}")

    try:
        parsed = parse_coordinates(coordinate)
        print(f"Parsed position {parsed}")
        print(f"Distance between {origin}, and {parsed}: "
              f"{distance_3d(origin, parsed)}")
    except Exception as e:
        print(f"Error parsing coordinates {e}")

    bad = "asd,zxc,qwe"
    print(f"\nParsing invalid coordinates: {bad}")

    try:
        parse_coordinates(bad)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X{x}, Y={y}, Z={z}")
