c = 1
for n in range(2943444, 2943529 + 1):
	c += 1
	for j in range(2, n // 2 + 1):
		if n % j != 0:
			print(n, c)
