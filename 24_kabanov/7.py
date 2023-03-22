with open("7.txt") as f:
    s = f.readline()
c = m = 0
for i in range(len(s) - 1):
    if (s[i] != "X" and s[i + 1] != "Y") or (s[i] != "X" and s[i + 1] != "Z"):
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
