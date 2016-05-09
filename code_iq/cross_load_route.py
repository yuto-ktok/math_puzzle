# -*- coding: utf-8 -*-
#nC1,nC2,,,と初めて偶数になるところを探す
n = int(raw_input())
ans = 0
for i in range(1, n) :
	if (n + 1 - i) % (2 * i) == 0 :
		ans = i
		break
print ans
