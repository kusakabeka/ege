def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
k = 0
maxd = 0
for i in range(125697, 190234 + 1):
    d = 2
    while d*d < i:
        if i % d == 0 and isprime(d) == True and isprime(i // d) == True:
            k += 1
            maxd = i
            break
        d += 1
print(k, maxd)