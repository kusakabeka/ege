from itertools import *
c = 0
for i in permutations('ПОЛИНА', r = 6):
	s = ''.join(i)
	for j in range(len(s) - 1):
		if (s[j] in 'ПЛН') and (s[j + 1] in 'ОИА'):
			c += 1
			print(s, c)