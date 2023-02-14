with open('6.txt') as f:
    s = f.readline()
c = 0
m = 0
s = s.replace('W', '*').replace('R', '*').replace('Q', '*')
for i in range(len(s)):
    if s[i] != '*':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)