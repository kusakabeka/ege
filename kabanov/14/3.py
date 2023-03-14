n = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 76
a = []
while n > 0:
    a = [n % 6] + a
    n = n // 6
print(abs(a.count(5) - a.count(0)))