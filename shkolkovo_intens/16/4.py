def f(n: int) -> int:
    if n < 3: return 2 * n * n + 2
    if n > 2 and n % 5 == 0: return 2 * f(n - 2) + f(n // 2)
    if n > 2 and n % 5 != 0: return 2 * n * n + f(n - 2) + 1 + f(n // 3)

print(f(100))