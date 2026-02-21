def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))

	def recursive(current, total):
		if current > total:
			print("Harvest time!")
			return
		print(f"Day {current}")
		recursive(current + 1, total)
	recursive(1, days)