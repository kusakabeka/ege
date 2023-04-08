def divs_list(number) -> list:
    divisiors_list = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
