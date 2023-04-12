from random import paretovariate
from xml.dom.xmlbuilder import DOMEntityResolver


def divs(number: int) -> int:
    divs = [i for i in range(2, number // 2 + 1) if number % i == 0]

    for j in divs:
        if j % 10 == 8 and j != 8:
            return divs
            
for n in range(500001, 10 ** 10):
    print(f"n: {n}\ndivisiors: {divs(n)}")
