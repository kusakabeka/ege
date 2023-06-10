c = 0
def f(n: int) -> int:
    if n > 32: return n * n * n
    if n <= 32: return f(n * 2) + f(n + 1) * n
for n in range(1, 1001):
    if str(f(n))[-1] == "3":
        c += 1
print(c)