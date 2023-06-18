def divisiors(n: int) -> list[int]:
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)

def func(arr: list[int]) -> bool:
    for i in range(1, n:)


for n in range(326496, 649632+1):
    d = divisiors(n)
    even = [x for x in d if x % 2 == 0]
    odd = [x for x in d if x % 2 != 0]
    if len(even) >= 70 and len(odd) >= 70 and len(even) == len(odd):
        print(n, min(x for x in d if x > 1000))



'''
450450 1001
589050 1050
630630 1001
'''