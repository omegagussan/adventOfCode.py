import itertools

def fill_pounds(s, chars):
	for p in map(iter, itertools.product(chars, repeat=s.count('?'))):
		yield ''.join(c if c != '?' else next(p) for c in s)


def test_valid(string: str, arrangement: list[int]):
	arrangement_idx = 0
	
	inside = 0
	for curr in list(string + "."):
		if arrangement_idx > len(arrangement):
			return False
		
		if curr == "#":
			inside += 1
		else:
			if 0 < inside:
				if arrangement_idx >= len(arrangement):
					return False
				if inside != arrangement[arrangement_idx]:
					return False
				arrangement_idx += 1
			inside = 0
			
	if arrangement_idx < len(arrangement):
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

if __name__ == "__main__":
	print(part1())
