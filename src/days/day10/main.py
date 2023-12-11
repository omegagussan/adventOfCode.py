import numpy as np
from itertools import pairwise


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
def parse(curr: str):
	match curr:
		case '|':
			return np.array([(1, 0), (-1, 0)])
		case '-':
			return np.array([(0, -1), (0, 1)])
		case 'L':
			return np.array([(0, -1), (1, 0)])
		case 'J':
			return np.array([(0, 1), (-1, 0)])
		case '7':
			return np.array([(0, -1), (-1, 0)])
		case 'F':
			return np.array([(0, 1), (1, 0)])
	return np.array([(0,0)])
			
def neighbours(pos, board):
	directions = np.array([([1], [0]), ([-1], [0]), ([0], [1]), ([0], [-1])])
	values = directions + pos
	return list(filter(lambda p: 0 <= p[0] <= board.shape[0] and  0 <= p[1] <= board.shape[1], values))


def get_value(pos, board):
	return board[(pos[0], pos[1])]

def part1():
	with open("sample.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		board = np.array([j for row in rows for j in row])
		board = board.reshape((len(rows[0]), len(rows)))
		start = [x for x in np.where(board == "S")]
	print(board)
	starts = list(filter(lambda x: get_value(x, board) != ".", neighbours(start, board)))
	curr = starts[0]
	visited = []
	while get_value(curr, board) != "S":
		print(" ")
		print(visited)
		print(curr)
		curr_symbol = get_value(curr, board)
		if curr_symbol == ".":
			print("should not happen!")
			break
		print(curr_symbol)
		connections = parse(curr_symbol)
		print(connections)
		next_poses = curr + connections
		print(next_poses)
		for pose in next_poses:
			str_pose = str(pose)
			if str_pose not in visited:
				curr = pose
				visited.append(str_pose)
				break
		
	return len(visited) // 2

if __name__ == "__main__":
	print(part1())
