from itertools import *
c = 0
for i in product('ABC', repeat=1): # 81 + 27 + 9 + 3
	s = "".join(i)
	c += 1
print(c)
