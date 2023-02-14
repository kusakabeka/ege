c = 0
for i in range(10000000, 100000000):
	s = str(i)
	for j in range(len(s) - 1):
		if (len(set(s)) == 8) and (int(s[j]) % 5 == 0) and ((int(s[j]) % 2 == 0 and int(s[j+1]) % 2 != 0) or (int(s[j]) % 2 != 0 and int(s[j+1]) % 2 == 0)):
			c += 1
			print(c)