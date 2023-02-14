def f(n): 
    if n == 1 : return 1
    return f(n - 1) * n
print("Please, enter number...")
n = int(input())
def new_func(f, n):
    print(f"factorial your number: {f(n)}")

