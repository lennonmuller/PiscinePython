import sys


def inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]

    if len(args) == 0:
        print("No items provided. Usage: python3"
              " ft_inventory_system.py item:qty ...")
        return

    inventory = {}

    for entry in args:
        if ":" not in entry:
            print(f"Invalid entry: {entry}")
            continue

        name, qty_str = entry.split(":")

        try:
            qty = int(qty_str)
        except Exception:
            print(f"Invalid quantity for item '{name}': {qty_str}")
            continue

        inventory[name] = qty

    if len(inventory) == 0:
        print("No valid intentory data provided.")
        return

    total_units = sum(inventory.values())
    print(f"Total items in inventory: {(total_units)}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    for name, qty in inventory.items():
        percent = (qty / total_units) * 100
        print(f"- {name}: {qty} units ({percent:.1f}%)")

    most = max(inventory.items(), key=lambda x: x[1])
    least = min(inventory.items(), key=lambda x: x[1])

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant item: {most[0]} ({most[1]} units)")
    print(f"Least abundant item: {least[0]} ({least[1]} units)")

    categories = {"Moderate": {}, "Scarce": {}}

    for name, qty in inventory.items():
        if qty > 3:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print("\n=== Management Suggestions ===")

    restock = [name for name, qty in inventory.items() if qty <= 1]

    if len(restock) > 0:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("No restocking needed.")

    print("\n=== Dicionary Properties Demo ===")

    keys_str = ""
    for k in inventory.keys():
        keys_str += k + ", "

    if len(keys_str) > 0:
        keys_str = keys_str[:-2]
    print(f"Dictionary keys: {keys_str}")

    values_str = ""
    for v in inventory.values():
        values_str += f"{v}, "

    if len(values_str) > 0:
        values_str = values_str[:-2]
    print(f"Dictionary values: {values_str}")

    sample_item = "sword"
    print(f"Sample lookup - '{sample_item}' "
          f"in inventory: {"sword" in inventory.keys()}")


if __name__ == "__main__":
    inventory_system()
