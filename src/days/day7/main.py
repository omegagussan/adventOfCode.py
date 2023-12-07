import collections
from functools import cmp_to_key, reduce

translations = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


def value_strength(val: str):
	return translations.get(val) if translations.get(val) is not None else int(
		val)


def hand_strength(vals: list[str]):
	most_common = collections.Counter(vals).most_common(2)[0]
	if most_common[1] == 5:
		return 6
	most_common, second_common = collections.Counter(vals).most_common(2)
	if most_common[1] == 4:
		return 5
	elif most_common[1] == 3 and second_common[1] == 2:
		return 4
	elif most_common[1] == 3:
		return 3
	elif most_common[1] == 2 and second_common[1] == 2:
		return 2
	elif most_common[1] == 2:
		return 1
	return 0


def compare(item1, item2):
	compare_hand = hand_strength(item1) - hand_strength(item2)
	if compare_hand == 0:
		for i in range(len(item1)):
			compare_card = value_strength(item1[i]) - value_strength(item2[i])
			if compare_card != 0:
				return compare_card
	return compare_hand


def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		hands = [row[:5] for row in rows]
		hand_to_bid = {row[:5]: int(row[6:]) for row in rows}
		hands = sorted(hands, key=cmp_to_key(compare), reverse=False)
		bid_rank_products = [(rank + 1) * hand_to_bid[hand] for (rank, hand) in
							 enumerate(hands)]
		return reduce((lambda x, y: x + y), bid_rank_products)


if __name__ == "__main__":
	print(part1())
