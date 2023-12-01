def part1():
	with open("input.txt") as input_file:
		sum = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			numbers = [c for c in row if c.isnumeric()]
			stiched = numbers[0] + numbers[-1]
			sum += int(stiched)
	return sum


translations = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}


def find_number(lst: list[str], backwards=False):
	remainder = ''
	state = list(reversed(lst)) if backwards else lst.copy()
	while True:
		elem = state.pop(0)
		if elem.isnumeric():
			return elem
		else:
			remainder += elem

		remainder_backwards = remainder[::-1]
		for k, v in translations.items():
			if remainder_backwards.startswith(
				k) if backwards else remainder.endswith(k):
				return str(v)


def part2():
	with open("input.txt") as input_file:
		sum = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			listan = [c for c in row]
			first = find_number(listan)
			last = find_number(listan, True)
			sum += int(first + last)
	return sum


if __name__ == "__main__":
	print(part1())
	print(part2())
