from collections import Counter

with open('10.txt') as f: s = f.readline()
ans = ''
for i in range(1, len(s) - 1):
    if s[i - 1] == s[i + 1]: ans += s[i]
print(Counter(ans))

