from collections import Counter
with open("1.txt") as f: a = [_.strip() for _ in f]

for i in range(len(a)): a[i] = a[i].replace("BU", "*")

c = 0

for i in range(len(a)):
	if Counter(a[i])["*"] > 3: c += 1

print(c)