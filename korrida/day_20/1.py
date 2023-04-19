for n in range(416782, 498324 + 1):
    divs = [i for i in range(2, n // 2 + 1) if n % i == 0]
    print(f"{n} -> {divs}, len = {len(divs)}")