with open('1.txt') as f:
	s = f.readline()
c = 0
for i in range(len(s)):
	if s[i] == 's':
		c += 1
print(c) 