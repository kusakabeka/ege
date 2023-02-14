from itertools import *

c = 0

for i in product('КАПКАН', repeat=6):
	s = ''.join(i)
	for j in range(len(s) - 1):
		if s[j] != s[j + 1]:
			print(s)
