def solve(file_name):
    with open(file_name) as f: n = int(f.readline()) ; a = [int(f.readline()) for _ in range(n)]
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1): prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    min_sum = min_len = float('inf')
    last_mod = {}
    last_mod[0] = 0
    for i in range(1, n + 1):
        mod = prefix_sum[i] % 321
        if mod in last_mod:
            j = last_mod[mod]
            if prefix_sum[i] - prefix_sum[j] < min_sum:
                min_sum = prefix_sum[i] - prefix_sum[j]
                min_len = i - j
            elif prefix_sum[i] - prefix_sum[j] == min_sum:
                min_len = min(min_len, i - j)
        last_mod[mod] = i

    print(min_len)

solve('27B.txt')