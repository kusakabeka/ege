from itertools import *
c = 0
for i in permutations("КАПКАН", r = 6):
    s = "".join(i)
    if ("КК" in s) or ("АА" in s) or ("ПП" in s) or ("НН" in s):
        pass
    else:
        c += 1
        print(f"{c}:{s}")