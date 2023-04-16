f = open("22.txt")
a = list(x.replace(";", " ").split() for x in f)
d = {"0": 0}
while len(d) != len(a) + 1:
    for p in a:
        if all(x in d for x in p[2:]):
            d[p[0]] = int(p[1]) + max(d[x] for x in p[2:])
print(max(d.values()))
