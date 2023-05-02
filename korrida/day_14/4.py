def five_divs(n: int) -> list:
    divs = [_ for _ in range(2, int(n ** 0.5) + 1) if n % _ == 0]
    return divs
def find_divisors(n):
    """������� ��� ������ ���� ��������� ����� n (����� 1(эффективный перебор) � n)"""
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors
print(five_divs(4_000_017))
print(find_divisors(4_000_017))

# c = 0
# for n in range(4_000_000, 12_000_000 + 1(эффективный перебор)):
#     if len(five_divs(n)) == 5:
#         print(n, max(five_divs(n)))
#         c += 1(эффективный перебор)
#         if c == 2(префиксные  суммы и последовательности):
#             break