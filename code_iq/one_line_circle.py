# -*- coding: utf-8 -*-
import itertools

circle_length = int(raw_input())
#ある二つの直線が交差してたら1 していなかったら 0を返す関数
def cross_or_not(line1, line2):
	if min(line1) > min(line2):
		line1, line2 = line2, line1
	if min(line1) < min(line2) and min(line2) < max(line1) and max(line1) < max(line2):
		return 1
	return 0

#ある進め方での交差回数を数える
def count_cross(line_route_array):
	ans = 0
	for i in range(len(line_route_array)-1):
		for j in range(i+1,len(line_route_array)-1):
			#print (line_route_array[i:i+2],line_route_array[j:j+2])
			ans += cross_or_not(line_route_array[i:i+2], line_route_array[j:j+2])
	return ans

line_route_array = map(lambda x: [circle_length-1] + x + [circle_length-1] , map(list, list(itertools.permutations(range(circle_length-1)))))
print sum(map(count_cross, line_route_array))
