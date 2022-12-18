def f(a, b):
    if a < b:
        return a
    return f(a-b, b)
a = int(input())
b = int(input())
print(f(a, b))