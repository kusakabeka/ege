arr = [int(input()) for _ in range(10)]
arr_1 = arr.copy()
arr_1 = [abs(_) for _ in arr_1]
arr[arr_1.index(max(arr_1))] *= -1
print(*arr, sep='\n')