f = open('17-4.txt')
a = list(map(int, f.readlines()))

sr = sum(a) / len(a)
c = 0
minsr = 10 ** 6

for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[i] % 10 == 5 and a[j] < sr) or (a[i] < sr and a[j] % 10 == 5):
            c += 1
            minsr = min(minsr, (a[i] + a[j]) // 2)
print(c, minsr)
