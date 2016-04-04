# -*- coding: utf-8 -*-
import Queue

BOARD_SIZE = 4

#boardは16桁文字列 1黒 -1白にする
#ex. "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1" 全部黒

#(row, col)をひっくり返す
def change_board(board, row, col):
	board_list = map(int,board.split(','))
	for i in range(BOARD_SIZE):
		board_list[ row * BOARD_SIZE + i] *= -1
	for i in range(BOARD_SIZE):
		board_list[ col + i * BOARD_SIZE] *= -1
	board_list[ row * BOARD_SIZE + col] *= -1
	return ",".join(map(str,board_list))

def print_board(board):
	board_list = map(int,board.split(','))
	for i in range(BOARD_SIZE):
		print board_list[(i*BOARD_SIZE): ((i + 1) * BOARD_SIZE)]
		print "\n"

#test change_board
#print_board(change_board("1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 0, 0))
#print_board(change_board("1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1", 1, 2))

#boradとqueueに初手(全部黒)を入れる
black_board = "1,"* (BOARD_SIZE * BOARD_SIZE - 1) + "1"
boards = {black_board : 0}
search_queue = Queue.Queue()
search_queue.put((black_board, 0))

def q39():
	while(not search_queue.empty()):
		(target_board, target_board_score) = search_queue.get() 
		for row in range(BOARD_SIZE):
			for col in range(BOARD_SIZE):
				next_board = change_board(target_board, row, col)
				#探索済みで、なければhashに入れる
				if next_board not in boards :
					boards[next_board] =  target_board_score + 1
					search_queue.put((next_board, target_board_score + 1))
	#boardからmaxのものを持ってくる
	return max(boards.items(), key=lambda x:x[1])
		
print q39()
