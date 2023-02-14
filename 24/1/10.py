from collections import Counter
with open('10.txt') as f: s = f.readline()
ans = ''
for i in range(len(s)): 
    if s[i] == 'A': ans += s[i + 1]
print(Counter(ans))