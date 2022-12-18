start = 5
fin = 49 
a = [0] * (fin + 1)
a[start] = 1
for i in range(start + 1, fin + 1):
    a[i] += a[i-1]
    if i % 3 == 0:
        a[i] += a[i//3]

print(a)





