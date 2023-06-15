with open("3.txt") as f: s = f.readline()
c = 0
for i in range(len(s) - 4):
    if s[i] == "M" and s[i + 4] == "M": c += 1
print(c)