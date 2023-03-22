def f(x, y):
    if x >= y: 
        return x == y 
    return f(x + 1, y) + f(x * 2, y)
print(f(2, 11)*f(11, 39) - f(2, 11)*f(11, 26)*f(26, 39))