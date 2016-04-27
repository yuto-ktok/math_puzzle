# -*- coding: utf-8 -*-
n = int(raw_input())
ans = 0
for i in range(1, n) :
	if (n + 1 - i) % (2 * i) == 0 :
		ans = i
		break
print ans