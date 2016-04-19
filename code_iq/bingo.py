# -*- coding: utf-8 -*-
input_value = []
def slice_five(num_list):
	return [num_list[i:i+5] for i in range(0,25,5)]

for i in range(4):
	input_value.append(slice_five(map(int,  raw_input().split(","))))

#print input_value
#数字列から12種類のbing配列を作る
def make_bingo_list(bingo_board):
	ans = []
	naname1 = []
	naname2 = []
	for i in range(5):
		ans.append(bingo_board[i][0:5])
		ans.append([bingo_board[j][i] for j in range(5)])
		naname1.append(bingo_board[i][i])
		naname2.append(bingo_board[i][4 - i])
	ans.append(naname1)
	ans.append(naname2)
	return ans

bingos = [make_bingo_list(i) for i in input_value]

min_value = 20
for i in range(12):
	for j in range(12):
		for k in range(12):
			for l in range(12):
				ans = len(set(bingos[0][i] + bingos[1][j] + bingos[2][k] + bingos[3][l]))
				if ans < min_value:
					min_value = ans
print min_value

