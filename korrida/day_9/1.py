def f(n):
    mas = []
    d = 2
    while d*d < n:
        if n % d == 0:
            mas.append(d)
            mas.append(n//d)
        d += 1
    if d*d == n:
        mas.append(d)
    return (mas)
for i in range (4234679, 10157812+1):
    if i**0.5 == int (i**0.5):
        mas = f(i)
        if len(mas) == 3:
            print (i,max(mas))


