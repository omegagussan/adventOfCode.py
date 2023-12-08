import collections
from functools import cmp_to_key, reduce, partial

translations = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
non_jokers = list(map(lambda x: str(x), range(2, 10)))
non_jokers.extend(["A", "K", "Q", "T"])


def value_strength(val: str, joker=False):
	if not joker and val == "J":
		return 0
	return translations.get(val) if translations.get(val) is not None else int(
		val)


cache = {}


def hand_strength(hand: str, joker=False):
	if not joker or not "J" in hand:
		most_common = collections.Counter(hand).most_common(2)[0]
		if most_common[1] == 5:
			return 6
		second_common = collections.Counter(hand).most_common(2)[1]
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

	if cache.get(hand, None):
		return cache[hand]
	joker_hands = []
	generate_all_jokers("", hand, 0, joker_hands)
	best = max(map(lambda x: hand_strength(x, False), joker_hands))
	cache[hand] = best
	return best


def generate_all_jokers(root: str, target: str, curr: int, res: list[str]):
	if curr == 5:
		res.append(root)
		return
	if target[curr] != "J":
		generate_all_jokers(root + target[curr], target, curr + 1, res)
	for c in non_jokers:
		generate_all_jokers(root + c, target, curr + 1, res)


def compare(item1, item2):
	compare_hand = hand_strength(item1) - hand_strength(item2)
	if compare_hand == 0:
		for i in range(len(item1)):
			compare_card = value_strength(item1[i]) - value_strength(
				item2[i])
			if compare_card != 0:
				return compare_card
	return compare_hand


def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		hands = [row[:5] for row in rows]
		hand_to_bid = {row[:5]: int(row[6:]) for row in rows}
		hands = sorted(hands, key=cmp_to_key(partial(compare, True)),
					   reverse=False)
		bid_rank_products = [(rank + 1) * hand_to_bid[hand] for (rank, hand) in
							 enumerate(hands)]
		return reduce((lambda x, y: x + y), bid_rank_products)


def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		hands = [row[:5] for row in rows]
		hand_strengths = [(hand, hand_strength(hand, True)) for hand in hands]
		hand_to_bid = {row[:5]: int(row[6:]) for row in rows}
		hands = sorted(hand_strengths, key=lambda x: x[1], reverse=False)
		print(hand_strengths)
		bid_rank_products = [(rank + 1) * hand_to_bid[hand] for (rank, hand) in
							 enumerate(hands)]
		return reduce((lambda x, y: x + y), bid_rank_products)


if __name__ == "__main__":
	# print(part1())
	print(part2())
