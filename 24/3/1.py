with open('1.txt') as f: s = f.readline()
m = 10000000
for i in range(len(s)):
    if ord(s[i]) % 2 != 0:
        m = max(m, ord(s[i]))
print(m)