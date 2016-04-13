# -*- coding: utf-8 -*-
import math
l = int(raw_input())
print l * sum(map(lambda x: x*(l-2-x), range(1,l-2))) * math.factorial(l-3)
