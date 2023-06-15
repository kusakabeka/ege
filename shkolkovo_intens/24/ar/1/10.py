with open("10.txt") as f: s = f.readline()

max_len_A, max_len_B = 0, 0
cur_len_A, cur_len_B = 0, 0

for i in range(len(s) - 1):
    if s[i] == "A" and s[i + 1] == "A":
        cur_len_A += 1
    else:
        max_len_A = max(max_len_A, cur_len_A)

for i in range(len(s) - 1):
    if s[i] == "B" and s[i + 1] == "B":
        cur_len_B += 1
    else:
        max_len_B = max(max_len_B, cur_len_B)

print(abs(max_len_A - max_len_B))