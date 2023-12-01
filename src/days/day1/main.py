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


def find_first_number(lst: list[str]):
	remainder = ''
	for i in range(len(lst)):
		elem = lst.pop(0)
		if elem.isnumeric():
			return elem
		else:
			remainder += elem

		for k, v in translations.items():
			if remainder.endswith(k):
				return str(v)


def find_last_number(lst: list[str]):
	remainder = ''
	for i in range(len(lst)):
		elem = lst.pop()
		if elem.isnumeric():
			return elem
		else:
			remainder += elem

		backwards_reminder = remainder[::-1]
		for k, v in translations.items():
			if backwards_reminder.startswith(k):
				return str(v)


def part2():
	with open("input.txt") as input_file:
		sum = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			first = find_first_number([c for c in row])
			last = find_last_number([c for c in row])
			sum += int(first + last)
	return sum


if __name__ == "__main__":
	print(part1())
	print(part2())
