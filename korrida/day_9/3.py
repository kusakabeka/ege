def divs(number) -> list:
    arr = []
    for i in range(1, number + 1):
        if number % i == 0: arr.append(i)
    return arr



for n in range(11275, 16328 + 1):
    if len(divs(n)) == 5:
        print(f"{divs(n)} ")
