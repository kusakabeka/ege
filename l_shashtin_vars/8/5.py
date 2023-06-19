c = 0
for n in range(1, 100000):
    o = oct(n)[2:]
    if n % 7 == 0:  o += o[-2:]
    else: o += oct((n % 7) * 7)[2:]
    
    r = int(o, 8)
    if r < 3000:
        c += 1
print(c)   