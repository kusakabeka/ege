# def is_prime(n: int) -> bool:
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             return False
#         d += 1
#     return True
# def divs(n: int) -> list:
#     return [_ for _ in range(2, n // 2 + 1) if n % _ == 0]
# def prime_number_check(arr: list):
#     if len(arr) == 2 and all((is_prime(d) for d in arr)):
#         return arr

# for n in range(523456, 578925 + 1):

def isprime(n):

    d = 2

    while d * d <= n:

        if n % d == 0:

            return False

        d += 1

    return True


k = 0

min1 = 500000

d1 = 0

d2 = 0

for i in range(523456, 578925 + 1):

    d = 2

    kd = 0

    while d*d < i:

        if i % d == 0:

            if isprime(d) == True and isprime(i // d) == True:

                if i / d - d < min1:

                    min1 = i / d - d

                    d1 = d

                    d2 = i / d

        d += 1

print(d1, d2)
