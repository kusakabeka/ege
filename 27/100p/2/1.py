with open("1B.txt") as f:
    n = int(f.readline())
    a = [int(_) for _ in f]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] < a[j]) and (a[i] + a[j]) % 10 == 0:
           counter += 1
print(counter)
