from collections import Counter
with open("4.txt") as f: s = f.readline()
ans = ""
for i in range(len(s) - 1):
    if s[i] == "X": ans += s[i+1]
print(Counter(ans))