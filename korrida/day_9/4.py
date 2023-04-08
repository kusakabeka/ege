def M(n):
    divisors = [i for i in range(2, n // 2 + 1) if n % i == 0]
    if not divisors: return 0
    else: return min(divisors) + max(divisors)

count = 0
for n in range(452021, 10**10):
    if M(n) % 7 == 3:
        print(n, M(n))
        count += 1
        if count == 5:
            break
# 452034 226019
# 452048 226026
# 452062 226033
# 452076 226040
# 452090 226047