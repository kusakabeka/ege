with open("1_a.txt") as f:
    s = f.readline()
a = [int(_) for _ in f]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        print(i, j)
