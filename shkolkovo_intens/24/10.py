with open("10.txt") as f: s = f.readline()
c = 0
for i in range(len(s) - 4):
    if (s[i] != s[i + 1]) and (s[i] != s[i + 2] and s[i + 1] != s[i + 2]) and (s[i] != s[i + 3] and s[i + 1] != s[i + 3] and s[i + 2] != s[i + 3]) and (s[i] != s[i + 4] and s[i + 1] != s[i + 4] and s[i + 2] != s[i + 4] and s[i + 3] != s[i + 4]):
        c += 1
print(c)