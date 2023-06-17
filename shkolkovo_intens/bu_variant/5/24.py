from collections import Counter
c = 0
with open("24.txt") as f: s = [_.rstrip() for _ in f]
for i in range(len(s)):
    if Counter(s[i])["Y"] > Counter(s[i])["T"]: c += 1
print(c)