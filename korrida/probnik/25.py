def min_div(number) -> int:
    i = 1
    for i in range(2, number):
        if number % i == 0:
            return i
            break


def max_div(number) -> int:
    maxx = 1
    for i in range(2, number // 2 + 1):
        if number % i == 0: maxx = i
    return maxx


for n in range(860_000, 10000000000):
    if max_div(n) != None and min_div(n) != None:
        M = max_div(n) - min_div(n)
    else:
        M = 0
    if M % 100 == 30:
        print(n, M)
