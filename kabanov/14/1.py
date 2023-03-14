n = 7 ** 103 + 20 * 7 ** 204 - 3 * 7 ** 57 + 97
a = []
while n > 0:
    a = [n % 7] + a
    n = n // 7
print(a.count(6)) # answer