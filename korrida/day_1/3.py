with open("3.txt") as f: s = f.readline().strip()
c = 1
m = 1
ms = s[0]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        m = max(m, c)
        