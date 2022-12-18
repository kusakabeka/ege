def f(x, n):
    if n == 0:
        return 1
    else:
        return x/n * f(x, n-1)
x = int(input())
n = int(input())
print('%.5f' % f(x, n))