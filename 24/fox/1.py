f = open("1.txt")
text = f.read()
c = 1
m = 0
for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)