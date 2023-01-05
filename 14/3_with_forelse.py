a = 1*26**4 + 3*26**3 + 5
b = 2*26**4 + 4*26**3 + 1*26 + 3
for x in range(0, 26):
    s = a + b + x*26
    for y in range(0, 26):
        sn = s + y*26**2 + y*26**2
        if sn % 8 != 0:
            break
    else:
        print((s+2*(2*26**2)) // 8)
