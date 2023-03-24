divs = lambda n: [_ for _ in range(1, n + 1) if n % _ == 0]
def search(num, divs, sumrest):
    if num == 0 or num == sumrest:
        return True
    if num < 0 or num > sumrest:
        return False
    return search(num - divs[0], divs[1:], sumrest - divs[0]) \
           or search(num, divs[1:], sumrest)

for n in range(300, 501):
    search(n, divs, )