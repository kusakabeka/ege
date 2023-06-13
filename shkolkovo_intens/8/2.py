c = 0
for i in range(100000, 1000000):
    if "5" in str(i) or "2" in str(i):
        c += 1
print(c)
