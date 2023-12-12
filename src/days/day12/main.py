import itertools

def fill_pounds(s, chars):
	for p in map(iter, itertools.product(chars, repeat=s.count('?'))):
		yield ''.join(c if c != '?' else next(p) for c in s)


def test_valid(string: str, arrangement: list[int]):
	groups = list(filter(lambda x: x, string.split(".")))
	if len(groups) != len(arrangement):
		return False
	for idx, g in enumerate(groups):
		if arrangement[idx] != len(g):
			return False
	return True

def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		total = 0
		for grid, values in [row.split() for row in rows]:
			arrangement = [int(y) for y in values.split(",")]
			g = fill_pounds(grid, "#.")
			valid = list(filter(lambda x: test_valid(x, arrangement), g))
			#print(g)
			#print(valid)
			#print(arrangement)
			#print(len(valid))
			#print(" ")
			total += len(valid)

	return total

def part2():
	with open("sample.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		total = 0
		for grid, values in [row.split() for row in rows]:
			arrangement = 5 * [int(y) for y in values.split(",")]
			unfolded = '?'.join(5 * [grid])
			g = fill_pounds(unfolded, "#.")
			valid = list(filter(lambda x: test_valid(x, arrangement), g))
			#print(g)
			#print(valid)
			print(arrangement)
			print(len(valid))
			#print(" ")
			total += len(valid)
	
	return total

if __name__ == "__main__":
	#print(part1())
	print(part2())
