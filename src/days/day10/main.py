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
			return [(1, 0), (-1, 0)]
		case '-':
			return [(0, -1), (0, 1)]
		case 'L':
			return [(0, 1), (-1, 0)]
		case 'J':
			return [(0, -1), (-1, 0)]
		case '7':
			return [(0, -1), (1, 0)]
		case 'F':
			return [(0, 1), (1, 0)]
			
def neighbours(pos, board):
	directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	values = [add(d, pos) for d in directions]
	return filter_in_board(values, board)


def filter_is_pipe(starts, board):
	return list(filter(lambda x: get_value(x, board) != ".", starts))


def filter_in_board(values, board):
	return list(filter(lambda p: 0 <= p[0] <= len(board) and 0 <= p[1] <= len(board[0]), values))

def add(t1, t2):
	return t1[0] + t2[0], t1[1] + t2[1]

def get_value(pos, board):
	return board[pos[0]][pos[1]]

def find_start(mat):
	for x, row in enumerate(mat):
		for idx, val in enumerate(row):
			if val == "S":
				return x, idx


def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		board = [list(row) for row in rows]
		start =  find_start(board)
	starts = filter_is_pipe(neighbours(start, board), board)

	curr_pose = starts[0]
	curr_val = get_value(curr_pose, board)
	visited = [str(curr_pose)]
	
	while curr_val != "S":
		next_poses = filter_in_board([add(curr_pose, c) for c in parse(curr_val)], board)
		for pose in next_poses:
			#because lists are not hashable
			str_pose = str(pose)
			#very ugly workaround to not just go to the goal. Sorry!
			if get_value(pose, board) == "S" and len(visited) == 1:
				continue
			elif str_pose not in visited:
				curr_pose = pose
				curr_val = get_value(curr_pose, board)
				visited.append(str_pose)
				break
		
	return len(visited) // 2


if __name__ == "__main__":
	print(part1())
