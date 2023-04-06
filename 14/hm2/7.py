for x in "0123456789abcd":
    for y in "0123456789abcdefg":
        n = int(f"131{x}1", 15) + int(f"13{y}3", 17)
        if n % 11 == 0:
            print(x)
