from itertools import *
c = 0
for i in product('АИОУЭ', repeat=6):
	s = "".join(i)
	c += 1
	if s[0] == "О" and s[-1] == "О":
		print(c)
