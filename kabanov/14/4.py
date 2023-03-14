n = 17 ** 5 + 85 ** 8 - 10 
a = []
while n > 0: a = [n % 17] + a ; n //= 17
print(a.count(16))