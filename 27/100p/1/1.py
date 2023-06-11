with open("1A.txt") as f:
    a = [int(_) for _ in f]
    controlNumber = a[-1]
    a = a[:-2]
# del 7 and not del 49
for i in a:
    if i % 7 != 0 and i % 49 == 0: a.remove(i)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if i * j % 