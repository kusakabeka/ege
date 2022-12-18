s = input()
c = 0
maxc = 0
if s[-1] == 'Р': s += 'О'
for i in range(len(s)):
    if s[i] == 'Р': c += 1
    else:
        maxc = max(maxc, c)
        c = 0
print(maxc)