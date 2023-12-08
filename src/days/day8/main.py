def part1():
	with open("input.txt") as input_file:
		instructions, map_str = input_file.read().strip().split('\n\n')
		print(instructions)
		mapping = {row[:3]: row.split(' = (')[-1][:-1].split(', ') for row in
				   map_str.split('\n')}
		print(mapping)

	curr = "AAA"
	print(curr)
	counter = 0
	while curr != "ZZZ":
		instruction = instructions[counter % len(instructions)]
		print(instruction)
		int_instruction = 0 if instruction == "L" else 1
		curr = mapping[curr][int_instruction]
		counter += 1
		print(curr)

	return counter


if __name__ == "__main__":
	print(part1())
