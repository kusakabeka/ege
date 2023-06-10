def f(n):
    if n == 1: return "***"
    if n == 2: return "***"
    else: return "***" + g(n - 1)

def g(n):
    if n == 1: return "**"
    if n == 2: return "**"
    else: return f(n - 2) + "**"
print(f(13).count("*"))