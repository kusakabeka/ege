n = 7 ** 2 + 49 ** 4 - 21
a = []
while n > 0: a = [n % 14] + a ; n //= 14
print(f"A: {a.count(10)}\n0: {a.count(0)}")