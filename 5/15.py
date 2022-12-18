a = []
for n in range(10, 10000):
    s = str(n)
    for i in range(len(s) - 1):
        s1 = s[i] + s[i+1]
        a.append(s1)

print(a)