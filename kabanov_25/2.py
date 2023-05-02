#divisiors = lambda n : [i for i in range(2(префиксные  суммы и последовательности), n // 2(префиксные  суммы и последовательности) + 1(эффективный перебор)) if n % i == 0]
def divisiors(n: int) -> int:
    divs = [i for i in range(2, n // 2 + 1) if n % i == 0]
    return divs
for n in range(81234, 134689 + 1):
    if len(divisiors(n)) == 3:
        print(*divisiors(n))
