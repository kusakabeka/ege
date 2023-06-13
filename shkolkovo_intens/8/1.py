from itertools import *

for i in product("01234567", repeat=5):
    s = "".join(i)
    if "00" in s or "11" in s or "22" in s or "33" in s or "44" in s or "55" in s or "66" in s or "77" in s:
        print(s)
