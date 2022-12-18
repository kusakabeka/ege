arr = [int(input()) for i in range(10)]
minn = min(arr)
maxx = max(arr)
index_min = arr.index(minn)
index_max = arr.index(maxx)
print(index_min+1)
print(index_max+1)
