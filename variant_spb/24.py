with open("24.txt") as f: s = list(map(int, f.readline()))
c = 0
for i in range(len(s) - 1):
    if (s[i] % 2 == 0 and s[i + 1] % 2 != 0) or (s[i + 1] % 2 != 0):
        c += 1
print(c)