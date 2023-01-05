a = 1 * 26 ** 4 + 3 * 26 ** 3 + 5
b = 2 * 26 ** 4 + 4 * 26 ** 3 + a * 26 + 3
for x in range(0, 26):
    s = a + b + x * 26
    flag = False
    for y in range(0, 26):
        s_n = s + y * 26 ** 2 + y * 26 ** 2
        if s_n % 8 != 0:
            flag = True
            break
    if flag == False:
        print(x, (s + (2*26**2)*2) % 8, (s+2*(2*26**2)) // 8) 
