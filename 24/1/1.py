with open('4.txt') as f:
	s = f.readline()
#print(s)
c = 0
m = 0
for i in range(len(s) - 2):
	if s[i] != 'Z':
		c += 1
	else:
		m = max(m, c)
		c = 0
print(m)