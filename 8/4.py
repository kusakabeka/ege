from itertools import *

c = 0

for i in product('АВДПР', repeat=4):
	s = ''.join(i)
	c += 1
	if 'А' not in s and len(set(s)) == 4:
		print(c, s)
