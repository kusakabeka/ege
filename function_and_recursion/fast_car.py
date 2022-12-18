arr = [int(input()) for _ in range(40)]
top_fast = arr[0]
arr_ind = []
for i in range(40):
    if arr[i] > top_fast:
        top_fast = arr[i]
for j in range(40):
    if arr[j] == top_fast:
        print(j+1)
        break
for j in range(40):
    if arr[j] == top_fast:
        ind = j
print(ind+1)