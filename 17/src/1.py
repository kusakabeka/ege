c = 0
min_cnt = 10000
for i in range(1107, 9504 + 1):
    if i % 9 == 0 and i % 7 != 0 and i % 15 != 0 and i % 17 != 0 and i % 19 != 0:
        c += 1
        min_cnt = min(min_cnt, i)
print(c, min_cnt)
