with open("6.txt") as f: s = f.readline()
c = 1
maxx = 0
for i in range(len(s)):
    if s[i].isdigit() and s[i + 1].isdigit():
        c += 1
        maxx = max(maxx, c)
    else:
        c = 0
print(maxx)