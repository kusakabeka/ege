def divisiors(n: int) -> list:
    divs = [i for i in range(2, n // 2 + 1) if n % i == 0]
    if len(divs) == 2:
        return divs

for n in range(174457, 174505 + 1):
    if divisiors(n) != None: print(*divisiors(n))
'''
[3, 58153]
[7, 24923]
[59, 2957]
[13, 13421]
[149, 1171]
[5, 34897]
[211, 827]
[2, 87251]

'''