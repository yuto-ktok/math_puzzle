# -*- coding: utf-8 -*-
import itertools

primitive_num_array = map(lambda x: x+1, range(9))

#全パターンlist化
num_array_patterns = map(list, list(itertools.permutations(primitive_num_array)))

#ある文字列の操作が終わるまでの回数を求める
def count_num_array(num_array):
	count = 0
	while num_array[0] != 1 :
		tmp = num_array[0]
		tmp_array = num_array[0 : tmp][::-1]
		num_array = tmp_array + num_array[tmp:]
		count += 1
	return count

max_count = 0
max_array = []
for num_array in num_array_patterns:
	count = count_num_array(num_array)
	if count > max_count :
		max_count = count
		max_array = num_array

print max_array
print max_count
