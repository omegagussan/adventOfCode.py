from collections import defaultdict

special_characters = set("!@#$%^&*()-+?_=,<>/")
used = 9999999999


def has_adjacent_symbol(schematic: dict, row: int, col: int, only_gear=False):
	indexes = [(row + 1, col + 1), (row, col + 1), (row - 1, col + 1),
			   (row + 1, col), (row - 1, col), (row, col - 1),
			   (row + 1, col - 1), (row - 1, col - 1)]
	values = map(
		lambda x: schematic.get(x) if schematic.get(x) else '.',
		indexes)
	return any(
		filter(lambda x: x in special_characters if not only_gear else x == '*',
			   values))


def get_adjacent_symbol(schematic: dict, row: int, col: int) -> \
	list[tuple[int, int]]:
	indexes = [(row + 1, col + 1), (row, col + 1), (row - 1, col + 1),
			   (row + 1, col), (row - 1, col), (row, col - 1),
			   (row + 1, col - 1), (row - 1, col - 1)]
	values = map(
		lambda x: (x, schematic.get(x) if schematic.get(x) else '.'),
		indexes)
	return [x[0] for x in values if x[1] == '*']


def build_dict(rows):
	return {(row_idx, col_idx): value for row_idx, row in enumerate(rows)
			for (col_idx, value) in enumerate(row)}


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		schematic = build_dict(rows)
	# add dot at end of each row so remainder don't wrap
	file_content = '.'.join(rows)
	# to compensate for hack above
	row_length = len(rows[0]) + 1
	remainder = ""
	for idx, val in enumerate(file_content):
		if remainder and not val.isnumeric():
			row = idx // row_length
			col = idx % row_length
			# print(val, row, col)
			# minus 1 is for we are actually at the char after the last part of the number
			indexes = [(row, col - x - 1) for x in range(len(remainder))]
			# print(indexes)
			if any(filter(lambda x: has_adjacent_symbol(schematic, x[0], x[1]),
						  indexes)):
				# print("im incrementing with " + remainder)
				total += int(remainder)
			else:
				print("skipping" + remainder)
			remainder = ""
		elif val.isnumeric():
			remainder += val
	return total


def part2():
	with open("sample.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		schematic = build_dict(rows)
	# add dot at end of each row so remainder don't wrap
	file_content = '.'.join(rows)
	# to compensate for hack above
	row_length = len(rows[0]) + 1
	remainder = ""
	gear_candidates = defaultdict(int)
	for idx, val in enumerate(file_content):
		if remainder and not val.isnumeric():
			row = idx // row_length
			col = idx % row_length
			# minus 1 is for we are actually at the char after the last part of the number
			indexes = [(row, col - x - 1) for x in range(len(remainder))]
			gears = list(set([i for x in indexes for i in
					 get_adjacent_symbol(schematic, x[0], x[1])]))
			if gears:
				print(gears)
				#print(indexes)
				print(remainder)
			for gear in gears:
				if gear_candidates[gear] == used:
					continue
				elif gear_candidates[gear] > 0:
					gear_ratio = (int(remainder) * int(gear_candidates[gear]))
					total += gear_ratio
					gear_candidates[gear] = used
					print("im incrementing with " + str(gear_ratio))
				else:
					print("I found:")
					print(gear)
					gear_candidates[gear] += int(remainder)
			remainder = ""
		elif val.isnumeric():
			remainder += val
	return total


if __name__ == "__main__":
	# print(part1())
	print(part2())
