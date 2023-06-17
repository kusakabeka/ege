min_len = 100000000
for n in range(51, 100000):
    s = "1" * n
    while "111" in s:
        s = s.replace("111", "22", 1)
        s = s.replace("222", "11", 1)
    if s.count("1") < min_len:
        min_len = s.count("1")
print(min_len)