def divs(n: int) -> list: return [i for i in range(2, n // 2 + 1) if n % i == 0]
c = 0
for n in range(2, 20000 + 1):
    if n < sum(divs(n)):
        c += 1
print(c)