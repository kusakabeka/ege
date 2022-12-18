def f(n):
    if n < 10:
        return n
    else:
        return max(n % 10, f(n // 10))

n = int(input())
print(f(n))