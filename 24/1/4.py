from collections import Counter
with open('4.txt') as f: s = f.readline()
ans = ''
for i in range(1, len(s)): 
    if s[i - 1] == 'X': ans += s[i]
print(Counter(ans))