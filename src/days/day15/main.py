from collections import defaultdict
import re


def part1():
	with open("input.txt") as input_file:
		parts = input_file.read().strip().split(',')
		return sum([eight_bit_hash(p) for p in parts])


def part2():
	with (open("input.txt") as input_file):
		parts = input_file.read().strip().split(',')
		hashmap = defaultdict(list)
		labelmap = defaultdict(list)
		for p in parts:
			label, _ = re.split('[-=]', p)
			if "-" in p:
				for box in labelmap[label]:
					label_pattern = p.replace("-", "=")
					tmp = [v for v in hashmap[box] if not v.startswith(label_pattern)]
					if not tmp == hashmap[box]:
						print("dropped " + p)
						print(tmp)
						print(hashmap[box])
						print(" ")
					hashmap[box] = tmp
				labelmap[label] = []
			else:
				if label == "tqjk":
					print("what")
				hash_label = eight_bit_hash(label)
				if not hashmap[hash_label]:
					hashmap[hash_label].append(p)
					labelmap[label].append(hash_label)
					continue
				else:
					tmp = [p if e.startswith(label + "=") else e for e in hashmap[hash_label]]
					if hashmap[hash_label] == tmp:
						hashmap[hash_label].append(p)
						hashmap[hash_label] = list(dict.fromkeys(hashmap[hash_label]))
						labelmap[label].append(hash_label)
						labelmap[label] = list(set(labelmap[label]))
					else:
						hashmap[hash_label] = tmp
		print(hashmap)
		return get_focusing_power(hashmap)


def matches_label(target, v):
	return target == v.split("=")[0]


def get_focusing_power(hashmap):
	s = 0
	for box, items in hashmap.items():
		for idx, i in enumerate(items):
			v = (int(box) + 1) * (idx + 1) * int(i[-1])
			s += v
	return s


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
	print(part2())
	#330336 HIGH
	#329680 HIGH