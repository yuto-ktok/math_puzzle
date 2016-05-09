# -*- coding: utf-8 -*-
from itertools import dropwhile, islice
print (lambda n:(list(islice(dropwhile(lambda i : (n + 1 - i) % (2 * i) != 0, range(1,n)),0,1)) + [0])[0])(int(raw_input()))
