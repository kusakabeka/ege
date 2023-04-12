def sum_divs(n: int) -> int:
    divs = [_ for _ in range(2, n // 2 + 1) if n % _ == 0]
    if not divs: return 0
    else: return max(divs) + min(divs)

c = 0
for n in range(250200, 10 ** 10):
    if sum_divs(n) % 123 == 17:
        print(n, sum_divs(n))
        c += 1
        if c == 5:
            break

'''

250212 125108
250458 125231
250593 83534
250621 35810
250704 125354

'''