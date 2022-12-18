arr = [int(input()) for _ in range(10)]
print(max(arr))
del arr[arr.index(max(arr))]
print(max(arr))