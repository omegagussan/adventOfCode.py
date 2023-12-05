from dataclasses import dataclass


@dataclass
class Rule:
	src: int
	dst: int
	span: int

	def apply(self, val: int):
		if self.src <= val < self.src + self.span:
			return self.dst + val - self.src
		return val


@dataclass
class RuleSet:
	name: str
	rules: list[Rule]

	def apply(self, val: int):
		tmp = val
		for rule in self.rules:
			old = tmp
			tmp = rule.apply(tmp)
			if old is not tmp:
				break
		return tmp

	def apply_all(self, vals: list[int]):
		return [self.apply(t) for t in vals]


def part1():
	with open("input.txt") as input_file:
		blocks = input_file.read().strip().split('\n\n')
		seed_str, *rest = blocks
		seeds = seed_str[7::].split(' ')
		rule_sets = [parse_rule_set(block) for block in rest]
		print(rule_sets)
		res = list(map(lambda x: int(x), seeds))
		for rules in rule_sets:
			res = rules.apply_all(res)
		return min(res)


def parse_rule_set(map_str):
	rules = []
	name, *rows = map_str.split('\n')
	for row in rows:
		dst, src, span = list(map(lambda x: int(x), row.split(' ')))
		rules.append(Rule(src, dst, span))
	return RuleSet(name, rules)


if __name__ == "__main__":
	print(part1())
