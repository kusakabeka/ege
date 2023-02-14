c = 1
for x in range(2, 11):
    n = 1234
    n1 = ''
    summ = 0
    maxx =0
    while n > 0:
        n1 += str(n % x)
        n //= x
    for i in range(0, len(n1)):
        summ += int(n1[i])
    c += 1
    print(f"{c} : {summ}")