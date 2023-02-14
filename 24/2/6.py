with open("6.txt") as f: s = f.readline()
c = 0
for i in range(len(s)):
    if s[i] == "(" and s[i+1] == ")":
        c += 1
print(c)
