# -*- coding: utf-8 -*-
import itertools
#import time

ans_hash = {}
circle_length = int(raw_input())


#ある二つの直線が交差してたら1 していなかったら 0を返す関数
def cross_or_not(line1, line2):
	if min(line1) > min(line2):
		line1, line2 = line2, line1
	if min(line1) < min(line2) and min(line2) < max(line1) and max(line1) < max(line2):
		return 1
	return 0

#進め方を線対称にする
def symmetricRoute(line_route):
	tmp = len(line_route) - 1 
	return [0] + map( lambda x: tmp - x, line_route[1:tmp]) + [0]


#ある進め方での交差回数を数える
def count_cross(line_route_array):
	tmp = str(line_route_array[::-1]) 
	if tmp in ans_hash:
		return ans_hash[tmp]
	tmp2 = str(symmetricRoute(line_route_array))
	if tmp2 in ans_hash:
		return ans_hash[tmp2]
	ans = 0
	for i in range(len(line_route_array)-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
		for j in range(i+1,len(line_route_array)-1):
			ans += cross_or_not(line_route_array[i:i+2], line_route_array[j:j+2])
	ans_hash[str(line_route_array)] = ans
	return ans

def count_cross2(route, line):
	ans = 0
	for i in range(len(route)-2):
		ans += cross_or_not(route[i: (i+2)],line)
	return ans

def count_cross3(route, not_marked , count):
	if len(not_marked) == 0:
		return count + count_cross2(route, [route[len(route)-1],0]);
	ans = 0
	for i in range(len(not_marked)): 
		next_point = not_marked[i]
		tmp = count_cross2(route, [route[len(route)-1],next_point])
		next_not_marked = not_marked[:]
		next_not_marked.pop(i)
		ans += count_cross3(route + [next_point], next_not_marked, count + tmp)
	return ans

#start = time.time()
line_route_array = map(lambda x: [0] + x + [0] , map(list, list(itertools.permutations(range(1,circle_length)))))

#pattern1
#print sum(map(count_cross, line_route_array))

#pattern2 実行時間 pattern1とそんな変わらす、、、 n=9 の時 1.7sぐらい,,,
if( circle_length % 2 == 1):
	ans = 0
	for i in range(1, (circle_length+1)/2):
		next_not_marked = range(1,circle_length)
		next_not_marked.pop(i-1)
		ans += count_cross3([0,i],next_not_marked,0)
	print ans * 2
else:
	print count_cross3([0],range(1,circle_length),0)
#print count_cross3([0],range(1,circle_length),0)
#elapsed_time = time.time() - start
#print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

