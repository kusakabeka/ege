c = 0
def f(n: int) -> int:
    if n < 32: return n * n + 15
    if n >= 32: return f(n / 2) + 15 + f(n - 1)
for n in range(1, 101):
    print(f"{hex(f(n))[2:]}")
