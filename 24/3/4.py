with open('4.txt') as f:
    s = f.read().strip()

n = len(s)
L = [1] * n

# Compute L using dynamic programming
for i in range(1, n):
    for j in range(i):
        if s[j] > s[i]:
            L[i] = max(L[i], L[j] + 1)

# Find the length of the longest decreasing subsequence
max_len = max(L)

# Backtrack through L to construct the subsequence
subseq = []
for i in range(n-1, -1, -1):
    if L[i] == max_len:
        subseq.append(s[i])
        max_len -= 1
        if max_len == 0:
            break

# Reverse the subsequence to get the correct order
subseq = subseq[::-1]

# Print the subsequence as a string
print(''.join(subseq))


