with open("17.txt") as f:
    a = [int(x) for x in f]

max_el = max([x for x in a if str(x)[-2:] == "15"])

for i in range(len(a) - 3):
    pass
