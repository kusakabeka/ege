from itertools import *
c = 0
for x in product("0123456", repeat=5):
    s = "".join(x)
    if s[0] != '0' and s.count('6') == 1:
        ch = s.count("2") * 2 + s.count("4") * 4 + s.count("6") * 6 # домножаем, чтобы найти сумму
        nch = s.count("1") + s.count("3") * 3 + s.count("5") * 5 # домножаем, чтобы найти сумму
        if ch < nch: c += 1
print(c)