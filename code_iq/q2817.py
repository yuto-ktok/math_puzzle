# -*- coding: utf-8 -*-
import copy
import time
vertical_line_board = [[0 for i in range(5)] for j in range(4)]
horizontal_line_board = [[0 for i in range(4)] for j in range(5)]
max_step_size = int(raw_input()) + 1

start = time.time()
def search_path(vertical_board, horizontal_board, row, col, step_count, before_step):
	#print "search" + str(row) + "," + str(col) + "step:" + str(step_count)
	if(step_count < max_step_size and row == 4 and col == 3):
		return 0
	if(step_count == max_step_size):
		if row == 4 and col == 3:
			return 1
		else:
			return 0
	ans = 0
	step_count += 1
	#search vertical path 
	if(before_step == 0 or before_step == 1):
		for next_row in range(5):
			#print "next search" + str(next_row) + "," + str(col)
			if check_vertical_path_enable(vertical_board, row, col, next_row):
				next_vertical_board = make_next_vertical_board(vertical_board, row, col, next_row)
				ans += search_path(next_vertical_board, horizontal_board, next_row, col, step_count, -1)

	#search horizontal path
	if(before_step == 0 or before_step == -1):
		for next_col in range(4):
			#print "next search" + str(row) + "," + str(next_col)
			if check_horizontal_path_enable(horizontal_board, row, col, next_col):
				next_horizontal_board = make_next_horizontal_board(horizontal_board, row, col, next_col)
				ans += search_path(vertical_board, next_horizontal_board, row, next_col, step_count, 1)
	return ans

def check_vertical_path_enable(vertical_board, row, col, next_row):
	if row == next_row:
		return False
	for i in range(min(row,next_row), max(row,next_row)):
		if vertical_board[i][col] != 0:
			return False
	return True

def make_next_vertical_board(vertical_board, row, col, next_row):
	next_vertical_board = copy.deepcopy(vertical_board)
	for i in range(min(row,next_row), max(row,next_row)):
		next_vertical_board[i][col] = 1
	return next_vertical_board

def check_horizontal_path_enable(horizontal_board, row, col, next_col):
	if col == next_col:
		return False
	for i in range(min(col,next_col), max(col,next_col)):
		if horizontal_board[row][i] != 0:
			return False
	return True

def make_next_horizontal_board(horizontal_board, row, col, next_col):
	next_horizontal_board = copy.deepcopy(horizontal_board)
	for i in range(min(col,next_col), max(col,next_col)):
		next_horizontal_board[row][i] = 1
	return next_horizontal_board

print search_path(vertical_line_board, horizontal_line_board, 0, 0, 0, 0)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
