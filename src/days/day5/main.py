from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class SeedSpan:
	frm: int
	to: int  # inclusive


@dataclass
class Rule:
	src: int
	dst: int
	span: int

	def apply(self, val: int):
		if self.src <= val < self.src + self.span:
			return self.dst + val - self.src
		return val

	def apply_span(self, val: SeedSpan):
		rule_upper = (self.src + self.span)
		if val.to < self.src or val.frm > rule_upper:
			return [val]
		else:
			parts = []
			if val.frm < self.src:
				parts.append(SeedSpan(val.frm, self.src-1))
			if val.to > rule_upper:
				parts.append(SeedSpan(rule_upper + 1, val.to))
			parts.append(SeedSpan(max(self.src, val.frm) - self.src + self.dst,
								  min(rule_upper,
									  val.to) - self.src + self.dst))
			return parts


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

	def apply_seed_spans(self, vals: list[SeedSpan]):
		tmp = []
		for rule in self.rules:
			tmp.extend([i for t in vals for i in rule.apply_span(t)])
		tmp = list(set(tmp))
		print(self.name)
		print(rule)
		print(tmp)
		print(" ")
		return tmp

	def apply_all(self, vals: list[int]):
		return [self.apply(t) for t in vals]


def part1():
	with open("input.txt") as input_file:
		blocks = input_file.read().strip().split('\n\n')
		seed_str, *rest = blocks
		seeds = seed_str[7::].split(' ')
		rule_sets = [parse_rule_set(block) for block in rest]
		res = list(map(lambda x: int(x), seeds))
		for rules in rule_sets:
			res = rules.apply_all(res)
		return min(res)


def part2():
	with open("sample.txt") as input_file:
		blocks = input_file.read().strip().split('\n\n')
		seed_str, *rest = blocks
		seed_blocks = list(map(lambda x: int(x), seed_str[7::].split(' ')))
		seeds = [
			SeedSpan(seed_blocks[i], seed_blocks[i] + seed_blocks[i + 1] - 1)
			for i in
			range(0, len(seed_blocks), 2)]
		rule_sets = [parse_rule_set(block) for block in rest]
		for rules in rule_sets:
			seeds = rules.apply_seed_spans(seeds)
		return min(list(map(lambda x: x.frm, seeds)))


def parse_rule_set(map_str):
	rules = []
	name, *rows = map_str.split('\n')
	for row in rows:
		dst, src, span = list(map(lambda x: int(x), row.split(' ')))
		rules.append(Rule(src, dst, span))
	return RuleSet(name, rules)


if __name__ == "__main__":
	print(part1())
	print(part2())
