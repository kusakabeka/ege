with open('7.txt') as f:
    s = f.readline()
c = 1
m = 1
s = s.replace('0', '*')
for i in range(1, len(s)):
    if s[i] != '*' or s[i] == '*' and s[i + 1] != '0':
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)