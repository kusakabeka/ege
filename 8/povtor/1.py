from itertools import *
c = 0
for i in product('АПРСУ', repeat=4):
	s = "".join(i)
	c += 1
	if 'А' not in s:
		print(c)
		break