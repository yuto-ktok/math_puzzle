# -*- coding: utf-8 -*-
import math

doubleShotArray = [[1, 2], [2, 3], [1, 4], [3, 6], [4, 7], [6, 9], [7, 8], [8, 9]]


#2枚抜きの組み合わせを求める
def calCombinationOfboubleShot(shotNum, shotArray):
	if(shotNum == 0):
		return 1
	if(len(shotArray) == 0):
		return 0

	ans = 0
	for i in range(len(shotArray)):
		shot = shotArray[i]
		#自分以前を除く
		nextShotCandidatesArray = shotArray[i+1:]
		nextShotArray = []
		#次の候補作成
		for j in range(len(nextShotCandidatesArray)):
			if(len(set(shot) & set(nextShotCandidatesArray[j])) == 0):
				nextShotArray.append(nextShotCandidatesArray[j])
		ans += calCombinationOfboubleShot(shotNum - 1, nextShotArray)
	return ans

def calPatternOfStrackOut():
	ans = 0
	for i in range(5):
		ans += math.factorial(9-i) * calCombinationOfboubleShot(i, doubleShotArray)
	return ans

print calPatternOfStrackOut()

