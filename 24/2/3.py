f = open('3.txt')
s = f.readline()
c = 1
m = 0
for i in range(len(s) - 1):
    if ord(s[i]) > ord(s[i + 1]):
        c += 1
        m = max(m, c)
    else: c = 1
print(m)
f.close()