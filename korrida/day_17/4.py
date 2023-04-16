def divs(number):
    return [i for i in range(2, number // 2 + 1) if number % i == 0]


c = 0
minn = 100 ** 10
for n in range(50_000_000, 60_000_000 + 1):
    if len(divs(n)) == 6 and 911 in divs(n):
        c += 1
        minn = min(minn, n)