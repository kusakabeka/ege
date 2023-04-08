from collections import Counter
with open("3.txt") as f: s = f.readline()
ans = ""
for i in range(1, len(s)):
	if s[i - 1] == "A" and s[i + 1] == "C":
		ans += s[i]
print(Counter(ans))