c = 0
for n in range(3, 51):
    a = []
    s = ">" + "1" * n + "2" * n + "3" * n
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s: s = s.replace(">1", "22>3", 1)
        if ">2" in s: s = s.replace(">2", "2>", 1)
        if ">3" in s: s = s.replace(">3", "11>2", 1)
    for i in s:
        if i.isdigit(): a.append(int(i))
    if sum(a) % 7 == 0: c += 1
print(c)