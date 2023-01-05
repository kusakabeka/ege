a = 7*25**5 + 2*25**3 + 3*25**2 + 5
b = 6*11**4 + 7*11**3 + 9*11
for x in range(0, 11):
    sx = a + b + x*25 + x*11**2
    for y in range(0, 11):
        sy = sx + y*25**4 + y
        if sy % 131 == 0:
            print(x, y, sy // 131)
