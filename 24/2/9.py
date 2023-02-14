with open('9.txt') as f: s = f.readline()
c = m = 0
for i in range(len(s) - 3):
    if s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y':
        c = 0
    else:
        c += 1
        m = max(m, c)
print(m)