''' через int '''
for x in "0123456789abcdefgh":
    a = int(f"9009{x}", 18) + int(f"2257{x}", 18)
    if a % 15 == 0: print(x, a // 15)

''' через разложение '''
for i in range(18):
    l = 11 * 18 ** 4 + 2 * 18 ** 3 + 5 * 18 ** 2 + 16 * 18 + 2 * x
    if l % 15 == 0: print(i, l // 15)