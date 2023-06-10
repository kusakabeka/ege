def f(n):
    if n <= 1: return n * 3
    else: return f(n - 2) + 2 * g(n - 1)
def g(n):
    if n <= 2: return n
    else: return g(n - 2) + 2 * f(n - 2) * f(n - 2)
print(f(5) + g(6))