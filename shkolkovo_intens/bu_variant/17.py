with open("17.txt") as f:
    a = [int(_) for _ in f]
c = 0
max_sum = 0
for i in range(len(a) - 1):
    if (a[i] % 7 == 0 and a[i] % 9 == 0 and a[i] % 10 == 3) and (() or ())