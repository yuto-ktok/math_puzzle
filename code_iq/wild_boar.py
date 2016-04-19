# -*- coding: utf-8 -*-

#入力のinput
board_size = int(raw_input())
board = []


def exchange_input(str):
	if str == "O":
		return 0
	else:
		return -1
	pass

board.append([ -1 for i in range(board_size+2)])
for i in range(board_size):
	board.append([-1] + map( exchange_input,  list(raw_input())) + [-1])
board.append([ -1 for i in range(board_size+2)])


def make_next_place(now_place, direction):
	row, col, step = now_place
	if direction == 0 :
		return (row + 1, col, step)
	elif direction == 1 :
		return (row - 1, col, step)
	elif direction == 2 :
		return (row, col + 1, step)
	elif direction == 3 :
		return (row, col - 1, step)


#あるイノシシの場所から一番遠い場所を求める
def cal_longest_load(board, startRow, startCol):
	ans = 0
	ans_board = [[-1 for i in range(board_size + 2)] for i in range(board_size + 2)]
	start_points = [(startRow, startCol, 0)]
	while len(start_points) > 0:
		start_point = start_points[0]
		del start_points[0]
		for i in range(4):
			now_point = start_point
			while True:
				now_point =  make_next_place(now_point, i)
				row, col, step = now_point
				#障害物なら終了
				if(board[row][col] == -1):
					break
				#未到達ならmarkする
				if(ans_board[row][col] == -1):
					ans_board[row][col] = 1
					#最長の経路ならans更新
					if ans < step:
						ans = step
					#先に障害物があればstart pointとして追加
					next_row, next_col, next_step =  make_next_place((row , col, step), i)
					if(board[next_row][next_col] == -1):
						start_points.append((row, col, step + 1))
	return ans
	
#すべてのイノシシの位置について最長の距離を求める
ans = 0
for row in range(board_size+2):
	for col in range(board_size+2):
		#障害物が置かれていたら無視する
		if(board[row][col] != -1):
			ans = max(ans, cal_longest_load(board, row, col))
print ans




