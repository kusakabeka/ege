def f(n: int) -> int:
    if n == 1: return 1
    elif n == 2: return 2
    else: return f(n - 1) + 3 * f(n - 2)
print(f(6))