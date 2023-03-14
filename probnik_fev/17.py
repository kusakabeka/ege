with open("17.txt") as f: s = list(map(int, f.readlines())) 
avg = abs(sum(s) / len(s))
c = m = 0
for i in range(len(s) - 2):
	if (s[i] < avg or s[i + 1] < avg or s[i + 2] < avg) and '9' in str(s[i]) and '9' in str(s[i + 1]) and '9' in str(s[i + 2]):
		c += 1
		m = max(m, s[i] + s[i+1] + s[i+2])
print(c, m)