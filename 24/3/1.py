with open('1.txt') as f: s = f.readline()
m = 100000000
for i in range(len(s)):
    if s[i].isdigit() and int(s[i]) % 2 != 0:
        m = min(m, int(s[i]))
print(m)