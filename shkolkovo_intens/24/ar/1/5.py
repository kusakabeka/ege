with open("5.txt") as f: s = f.readline().split("+")
print(sum([int(_) for _ in s]))