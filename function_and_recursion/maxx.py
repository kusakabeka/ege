m = int(input())
arr = [int(input()) for _ in range(10)]
summ = 0
c = 0
for i in range(10):
    if arr[i] <= m:
        summ += arr[i]
        c += 1
if c != 0:
    res = summ / c
