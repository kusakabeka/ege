from itertools import *
c = 0
for i in product('ЛНОС', repeat=5):
	s = "".join(i)
	c += 1
	if c == 1020:
		print(s)
		break