from functools import reduce

def rotate_matrix(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def flatmap(reverse):
	return [a for b in reverse for a in b]

def transpose(mat):
	return [list(i) for i in zip(*mat)]

def tilt(mat):
	mat_t = transpose(mat)
	for idx in range(1, len(mat)):
		row = mat[idx]
		row_indexes = list(map(lambda x: x[0], filter(lambda x: x[1] == "O", enumerate(row))))
		for row_idx in row_indexes:
			path = mat_t[row_idx][:idx]
			blockers_on_path = list(map(lambda x: x[0], filter(lambda x: x[1] != ".", enumerate(path))))
			if not blockers_on_path:
				blockers_on_path = [-1]
			target_idx = blockers_on_path[-1] + 1 # because we place it on the next spot
			if target_idx == idx:
				continue
			mat_t[row_idx][target_idx] = "O"
			mat_t[row_idx][idx] = "."
			mat = transpose(mat_t)
	return mat
def part1():
	total = 0
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		mat = [list(row) for row in rows]
		mat = tilt(mat)
		max_leverage = len(mat)
		for idx, row in enumerate(mat):
			count = len(list(filter(lambda x: x == "O", row)))
			total += (max_leverage - idx) * count
	return total

def part2():
	total = 0
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		mat = [list(row) for row in rows]
		mat = tilt(mat)
		max_leverage = len(mat)
		for idx, row in enumerate(mat):
			count = len(list(filter(lambda x: x == "O", row)))
			total += (max_leverage - idx) * count
	return total

def count_rocks(mat):
	is_rocks = list(map(lambda x: 1 if x == "O" else 0, flatmap(mat)))
	return reduce(lambda x, y: x + y, is_rocks)


if __name__ == "__main__":
	print(part1())
	print(part2())
