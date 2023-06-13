def f(n):
    if n <= 15: return 2 * n * n + 4 * n + 3
    if n > 15 and n % 3 == 0: return f(n - 1) + n * n + 3
    if n > 15 and n % 3 != 0: return f(n - 2) + n - 6
c = 0
for n in range(1, 1001):
    if f(n) % 2 != 0:
        c += 1
print(c)