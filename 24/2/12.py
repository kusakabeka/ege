with open('12.txt') as f: s = f.readline()
c = m = 0
for i in range(len(s)-1):
    if s[i] == '0' and s[i + 1] == '0':
        c = 1
    else:
        c += 1
        m = max(m, c)
print(m)

