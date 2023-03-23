maxx = 0
for n in range(200, 100000):
    s = "1" * n
    while "1111" in s:
        s = s.replace("1111", "22", 1)
        s = s.replace("222", "1", 1)
    if 8
    maxx = max(maxx, len(s))
        print(n)
        break