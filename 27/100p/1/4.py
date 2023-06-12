with open("4B.txt") as f: n = int(f.readline()) ; arr = [int(_) for _ in f]
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
     5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for num in arr:
    num_str = str(num) 
    for digits in num_str:
        d[int(digits)] += 1

print(max(d, key=d.get))

