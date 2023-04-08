def divs_list(number):
    arr = []
    for i in range(2, number // 2 + 1):
        if number % i == 0: arr.append(i)
    return arr


for n in range(174457, 174505 + 1):
    if len(divs_list(n)) == 2:
        print(f"{n} --> {divs_list(n)}")
