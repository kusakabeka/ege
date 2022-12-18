arr = [int(input()) for _ in range(60)]

minimal = 10 ** 9
cnt = 0

for i in range(60):
    if arr[i] < minimal:
        minimal = arr[i]
        cnt += 1
