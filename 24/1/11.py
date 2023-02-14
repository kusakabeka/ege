from collections import Counter
with open('11.txt') as f: s = f.readline()
ans = ''
for i in range(1, len(s)):
    if s[i] == 'A' and s[i + 1] == 'D': ans += s[i-1]
print(Counter(ans)) 