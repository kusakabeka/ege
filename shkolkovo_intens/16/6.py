def f(n: int) -> int:
    if n < 6: return 2 * n + 1
    if n > 5 and n % 3 == 0: return 3 * f(n - 1) + f(n // 2) + n
    if n > 5 and n % 3 != 0: return 5 * n * n + f(n - 1) + f(n // 2)
for n in range(1, 1001):
    if f(n) % 10 == 8:
        print(n)
        break