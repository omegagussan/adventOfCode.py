threshold = {
	"red": 12,
	"green": 13,
	"blue": 14
}


def check(color_claim: str):
	color = color_claim.split(' ')[1]
	return threshold[color] >= int(color_claim.split(' ')[0])


def update_max(color_claim: str, maxes):
	color = color_claim.split(' ')[1]
	if maxes[color] < int(color_claim.split(' ')[0]):
		maxes[color] = int(color_claim.split(' ')[0])


def part1():
	with open("input.txt") as input_file:
		total = 0
		games = input_file.read().strip().split('\n')
		for game in games:
			failed = False
			claims = ''.join(game.split(': ')[1]).split("; ")
			for claim in claims:
				color_claim = claim.split(', ')
				if any(map(lambda x: not check(x), color_claim)):
					failed = True
					break
			# add row number if success
			if not failed:
				total += int(''.join(game.split(': ')[0]).split(' ')[1])
	return total


def part2():
	with open("input.txt") as input_file:
		total = 0
		games = input_file.read().strip().split('\n')
		for game in games:
			maxes = {"red": 0, "blue": 0, "green": 0}
			claims = ''.join(game.split(': ')[1]).split("; ")
			for claim in claims:
				color_claims = claim.split(', ')
				for color_claims in color_claims:
					update_max(color_claims, maxes)
			total += maxes["green"] * maxes["blue"] * maxes["red"]
	return total


if __name__ == "__main__":
	print(part1())
	print(part2())
