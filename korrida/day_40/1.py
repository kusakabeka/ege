with open("1B.txt") as f:
    n = int(f.readline())
    a = [int(i) for i in f]

odd = []
even = []
for i in range(len(a)):
    if a[i] % 2 == 0: even.append(a[i])
    else: odd.append(a[i])
min_odd_1 = min(odd); odd.remove(min_odd_1)
min_odd_2 = min(odd)
min_even_1 = min(even); even.remove(min_even_1)
min_even_2 = min(even)
print(f"odd sum: {min_odd_1 + min_odd_2}, even sum: {min_even_1 + min_even_2}")
# odd sum: 2, even sum: 172
