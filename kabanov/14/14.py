for x in range(1, 51):
    b = bin(x)[2:]
    if len(b) >= 3 and b[-3] + b[-2] + b[-1] == "011": print(x)
