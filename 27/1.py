n = int(input())
a = []
s = 0
m = 0
for i in range(7):
	a.append(int(input()))
for i in range(7, n):
	x = int(input())
	if a[i % 7] > m: m = a[i % 7]
	if x + m > s:
		s = x + m
	a[i % 7] = x
print(s)


