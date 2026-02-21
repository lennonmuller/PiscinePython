def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seeds = seed_type.capitalize()
	if unit == "packets":
		print(f"{seeds} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{seeds} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{seeds} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")