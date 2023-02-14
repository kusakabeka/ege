from itertools import *
c = 0
for i in product('УОА', repeat=5):
	s = "".join(i)
	c += 1
	if c == 100:
		print(s)
