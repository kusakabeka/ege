import mpmath

mpmath.mp.dps = 50 # устанавливаем точность в 50 знаков после запятой
s = mpmath.power('0.66796875', 20000000014)
print(hex()[2:])
