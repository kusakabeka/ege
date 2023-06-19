count = 0
for line in open("9.txt"):
    arr = sorted(map(int, line.strip()))
    if len(set(arr)) == 6 and 5 * (arr[0] + arr[-1]) >= 3 * sum(arr[1:-1]):
        count += 1
print(count)        