def is_prime(n: int) -> bool:
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def divs(n: int) -> list:
    return [_ for _ in range(2, int(n ** 0.5) + 1) if n % _ == 0]


def count_prime_number(arr: list) -> int:
    count = 0
    for i in arr:
        if is_prime(i): count += 1
    return count


def max_prime_number(arr: list) -> int:
    m = 0
    for j in arr:
        if is_prime(j): m = max(m, j)
    return m


for n in range(25317, 51237 + 1):
    if count_prime_number(divs(n)) >= 6:
        print(n, max_prime_number(divs(n)))

'''

30030 13
39270 17
43890 19
46410 17

'''
