from itertools import *
c = 0
for i in product("АВДПР", repeat=4):
	s = ''.join(i)
	c += 1
	if 'А' not in s:
		s1 = s
		