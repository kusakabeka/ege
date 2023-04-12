'''
if max_div(n) == none or min_div(0) == none: M = 0
else: M = max_div(n) - min_div(0)
'''


def M(number) -> int:
    divs = [i for i in range(2, number // 2 + 1) if number % i == 0]
    if not divs:
        return 0
    else:
        return max(divs) - min(divs)


count = 0
for n in range(860_000, 10 ** 10):
    if M(n) % 100 == 18:
        print(n, M(n))
        count += 1
        if count == 5:
            break
'''

860040 430018
860163 286718
860219 27718
860240 430118
860440 430218

'''
