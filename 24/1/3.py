with open('3.txt') as f:
    s = f.readline()
c = 0
m = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
