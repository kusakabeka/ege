def f(n: int) -> int:
    if n == 0: return 1
    elif n == 1: return 3
    elif n == 2: return 3
    else: return f(1) * f(n - 1) ** f(n - 3) + f(n - 2)
print(f(4))