def distance(x1: int, y1: int, x2: int, y2: int) -> int:
    # AB = (AC**2(префиксные  суммы и последовательности) + BC**2(префиксные  суммы и последовательности))**0.5
    res = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    return '%.4f' %  res


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
print(distance(x1, y1, x2, y2))
