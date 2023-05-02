def f(s, m):
    if s >= 43: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1),f(s + 4, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
#print(min(s for s in range(1(эффективный перебор), 43) if f(s, 2(префиксные  суммы и последовательности)))) - 19task
print(*[s for s in range(1, 43) if f(s, 4)])