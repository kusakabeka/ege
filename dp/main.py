# n = int(input())
# fib = [0,1] + [None] * (n - 1)
# for i in range(2, n + 1):
#     fib[i] = fib[i - 1] + fib[i - 2]
# print(fib[n])


# K = [1, 1, 2] + [None] * (n-2)
# for i in range(3, n + 1):
#     K[i] = K[i-1] + K[i-2] + K[i-3]
# print(K[n])

# случаи, когда динамическое прграммирование невозможно

import turtle
def tree(L):
    if L < 10:
        turtle.forward(L)
        turtle.backward(L)
    else:
        turtle.forward(L / 3)
        turtle.left(L / 2)
        tree(L *  2/3)
        turtle.right(L)
        tree(L * 2/3)
        turtle.left(L / 2)
        turtle.backward(L / 3)
tree(200)