with open("1.txt") as f:
    numb_cells = int(f.readline())
    numb_passeng = int(f.readline())
    a = []
    for i in range(numb_passeng):
        st, end = map(int, f.readline().split())
        a.append([st, end])
a.sort()

# время окончания хранения багажа в ячейках
camera = [0] * numb_cells
count = 0
last_cells = 0
for i in range(numb_passeng):
    st, end = a[i]
    for j in range(numb_cells):
        if camera[j] < st: # если T(окончания хранения багажа) < времени сдачи, то это означает, что ячейка свободна
            camera[j] = end # записываем время освобождения ячейки (end) в camera[j] => данная ячейка будет занята до указанного времени
            count += 1 # один пассажир успешно разместил свой багаж
            last_cells += j + 1 # добавляем номер ячейки к переменной last_cells
            break
print(count, last_cells)
#344 35119