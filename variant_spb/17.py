with open("17.txt") as f: s = list(map(int, f.readlines()))
mx = []
c = 0
maxx = 0
for i in s:
    if i % 10 == 5: mx.append(i)
for i in range(len(s) - 1):
    if ((s[i] % 10 == 5 and s[i + 1] % 10 != 5) or (s[i] % 10 != 5 and s[i + 1] % 10 == 5)) and \
            (abs(s[i] ** 2 - s[i + 1] ** 2) <= max(mx) ** 2):
        c += 1
        maxx = max(maxx,abs(s[i] ** 2 - s[i + 1] ** 2))
print(c, maxx)