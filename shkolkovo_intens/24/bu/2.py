with open("test.txt") as f: a = [l.rstrip() for l in f]
c = 0
for i in range(len(a)):
    a[i] = a[i].replace("SY", "*")
for i in range(len(a)):
    if a[i].count("*") > 2:
        c += 1
print(c)
