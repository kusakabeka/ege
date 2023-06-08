from collections import Counter
with open("1.txt") as f: a = [_.strip() for _ in f]
c = 0
for i in range(len(a)):
	if Counter(a[i])["K"] < Counter(a[i])["O"]:
		c += 1
print(c)
