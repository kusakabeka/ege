n = 7 ** 103 + 6 * 7 ** 104 - 3 * 7 ** 57 + 98
a = []
while n > 0:
    a = [n % 7] + a
    n = n // 7
print(sum(6)) # answer