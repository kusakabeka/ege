def g(n):
    if n < 2: return 1
    if n > 1: return f(n - 1) + 2 * g(n - 1)
def f(n):
    if n < 2: return 1
    if n % 2 != 0 and n > 1: return f(n - 1) + g(n - 1)
    if n % 2 == 0 and n > 1: return f(n - 2) + g(n - 2)
print(f(25) - g(25))
