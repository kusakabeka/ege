from collections import Counter

with open("1.txt") as f: s = f.readline()
ans = ""
for i in range(len(s) - 2):
	if s[i + 1] == "A" and s[i + 2] == "D":
		ans += s[i]
print(Counter(ans))
