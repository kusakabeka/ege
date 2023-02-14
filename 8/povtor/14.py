from itertools import *

c = 0

for i in product('АНДРЕЙ', repeat=6):
	s = ''.join(i) # ЕЕДЕДН
	if s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' and (s[0] == ''):