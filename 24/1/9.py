with open('9.txt') as f:
    s = f.readline()
c, m  = 0, 1
s = s.replace('ZZ', '*').split('*')
for i in range(len(s)- 1):
    if (s[i] != '*') or (s[i] != '*' and s[i + 1] != '*'):
        c += 1
        m = max(m, c)
    else:
        c = 0
print(s)        