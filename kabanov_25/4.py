def divs(n: int) -> set:
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d = {i, n // i}
    return sorted(d)

print(divs(98))