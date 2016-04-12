# -*- coding: utf-8 -*-
import math
l = int(raw_input())
print l * sum(map(lambda x: x*(l-3), range(1,l-2))) * math.factorial(l-3)
