def f(n: int) -> int:
    if n > 25: return 2 * n * n * n + n * n
    if n <= 25: return f(n + 1) + 5 * f(n + 3)
summ = 0
for i in str(f(2)):
    summ+= int(i)
print(summ)