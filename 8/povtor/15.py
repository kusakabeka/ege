from itertools import *
c = 0
for i in product("ИГОРЬ", repeat=8):
	s = ''.join(i)
	if s.count('О') == 1 and s.count('Ь') == 1 and s[0] != 'Ь':
		c += 1
print(c)