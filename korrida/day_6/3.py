import re
c = 0
a = []
with open("3.txt") as f: s = f.readline().replace("AB", "*")
for i in range(len(s)):
	if s[i] == "*":
		nac = tuple(s[i])
		c += 1
		if c == 21:
