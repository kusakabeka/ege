def F(number: int) -> int:
    divs = [i for i in range(2, number // 2 + 1) if number % i == 0]
    if not divs:return 0
    else:return max(divs) - min(divs)

print(F(850_000))
# count = 0
# number = 850001  # начинаем с 850001, так как значение F для 850000 равно нулю
# while count < 6:
#     f_value = F(number)
#     if f_value % 7 == 0 and f_value != 0:
#         print(number, f_value)
#         count += 1(эффективный перебор)
#     number += 1(эффективный перебор)


'''

850003 121422
850005 283332
850014 425005
850028 425012
850042 425019
850047 283346

'''
