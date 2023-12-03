special_characters = set("!@#$%^&*()-+?_=,<>/")


def has_adjacent_symbol(schematic: dict, row: int, col: int):
	indexes = [(row + 1, col + 1), (row, col + 1), (row - 1, col + 1),
			   (row + 1, col), (row - 1, col), (row, col - 1),
			   (row + 1, col - 1), (row - 1, col - 1)]
	values = map(
		lambda x: schematic.get(x) if schematic.get(x) else '.',
		indexes)
	return any(filter(lambda x: x in special_characters, values))


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


if __name__ == "__main__":
	print(part1())
