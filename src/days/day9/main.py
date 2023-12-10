from itertools import pairwise
from functools import reduce


def part1():
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')
        res = []
        for row in rows:
            values = [int(v) for v in row.split(' ')]
            diffs = [values]
            while not last_diff_is_all_zeroes(diffs):
                last_diffs = diffs[-1]
                diffs.append([b - a for a, b in pairwise(last_diffs)])
            for idx in reversed(range(0, len(diffs) - 1)):
                print(idx)
                new_val = diffs[idx][-1] + diffs[idx + 1][-1]
                diffs[idx].append(new_val)
            res.append(diffs[0][-1])
    print(res)
    return reduce((lambda x, y: x + y), res)


def last_diff_is_all_zeroes(diffs):
    last_diff = diffs[-1]
    zeroes = list(map(lambda x: x == 0, last_diff))
    return all(zeroes)


if __name__ == "__main__":
    print(part1())
