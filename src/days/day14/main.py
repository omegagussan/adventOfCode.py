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
			rest_idx = list(map(lambda x: x[0], filter(lambda x: x[1] != ".", enumerate(path))))
			if not rest_idx:
				rest_idx = [-1]
			target_idx = rest_idx[-1] + 1
			mat_t[row_idx][target_idx] = "0"
			mat_t[row_idx][idx] = "."
			mat = transpose(mat_t)
	return mat
def part1():
	total = 0
	with open("sample.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		mat = [list(row) for row in rows]
		mat = tilt(mat)
		max_leverage = len(mat)
		for idx, row in enumerate(mat):
			print(row)
			count = len(list(filter(lambda x: x == "0", row)))
			print(count)
			total += (1 + max_leverage - idx) * count
	return total


if __name__ == "__main__":
	print(part1())
