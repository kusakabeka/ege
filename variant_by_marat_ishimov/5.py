def to_3(n: int) -> str:
    ans = ""
    while n > 0: ans += str(n % 3); n //= 3
    return ans[::-1]
for n in range(10, 1000):
    t = to_3(n)
    if n % 2 == 0:
        t += t[-2:]
    else:
        t += to_3(sum(map(int, list(t))))
    r = int(t, 3)
    print(f"n: {n} -> r: {r} ")