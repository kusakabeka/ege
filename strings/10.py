with open('24.txt') as f:
    a = list(f.readline())
c = 0
for i in range(len(a)):
    c += 1
    if c == 1023: print(f"{a[i]} --> {c}"); break