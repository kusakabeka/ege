def f(x: int, y: int):
    if x < y: 
        return 0
    if x == y: 
        return 1
    if x < y:
        return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)
print(f(..., ...) * f(..., ...))

