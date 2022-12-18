def fib(num: int) -> int:
    if num < 3:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


n = int(input())
print(fib(n))
