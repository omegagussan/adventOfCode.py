import math


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			winners, candidates = row.split(": ")[1].split(" | ")
			overlap = set(winners.split()).intersection(candidates.split())
			points = int(math.pow(2, len(overlap) - 1)) if overlap else 0
			total += points
	return total


def part2():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		original = {int(row.split(": ")[0][5::]): row.split(": ")[1].strip() for row in rows}
		print(original)
		stack = list(original.items())
		while stack:
			nr, row = stack.pop(0)
			total += 1
			winners, candidates = row.split(" | ")
			overlap = set(winners.split()).intersection(candidates.split())
			indexes = [int(nr) + index + 1 for index in range(len(overlap))]
			for index in indexes:
				stack.append((index, original.get(index)))
	return total


if __name__ == "__main__":
	print(part1())
	print(part2())
