import math


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			winners, candidates = row.split(": ")[1].split(" | ")
			print(winners)
			print(candidates)
			overlap = set(winners.split()).intersection(candidates.split())
			points = int(math.pow(2, len(overlap) - 1)) if overlap else 0
			print(points)
			print(" ")
			total += points
	return total


if __name__ == "__main__":
	print(part1())
