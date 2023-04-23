f = open("27_A.txt")
n = [int(_) for _ in f]
c = 0
for i in range(1, len(n)):
    for j in range(i+1, len(n)):
        if ((n[i] + n[j]) % 80 == 0) and (n[i] > 50 or n[j] > 50):
            c += 1
print(c)
f.close()
