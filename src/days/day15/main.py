def part1():
	with open("input.txt") as input_file:
		parts = input_file.read().strip().replace('/n', '').split(',')
		return sum([eight_bit_hash(p) for p in parts])


def eight_bit_hash(string: str) -> int:
	val = 0
	for char in string:
		val += ord(char)
		val *= 17
		val = val % 256
	return val

if __name__ == "__main__":
	#print(eight_bit_hash("HASH"))
	print(part1())