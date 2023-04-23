f = open("26.txt")
n = int(f.readline())
a = [int(_) for _ in f]
arr = []
for i in range(n):
	for j in range(i + 1, n):
		if s[j] - s[i] >= 3:
			... 