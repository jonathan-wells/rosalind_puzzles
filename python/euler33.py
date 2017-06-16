#!/usr/bin/env python3

from fractions import Fraction

def iscurious(n, d):
    n, d = str(n), str(d)
    if n[0] == n[1] or d[0] == d[1]:
        return False

    common = set(n).intersection(set(d))
    if common == set():
        return False
    else:
        common = str(common)

    smalln, smalld = n.strip(common), d.strip(common)
    if smalln == '' or smalld == '':
        return False

    n, d, smalln, smalld = [int(i) for i in (n, d, smalln, smalld)]
    if smalld == 0:
        return False
    else:
        return bool(smalln/smalld == n/d)

def findcurious():
    curious = []
    for n in range(10, 100):
        for d in range(n+1, 100):
            if n%10 != 0 and d%10 != 0 and iscurious(n, d):
                curious.append((n, d))
    return curious

def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

def prodinlowesterms():
    curious = findcurious()
    print(curious)
    nprod = product([i[0] for i in curious])
    dprod = product(i[1] for i in curious)
    print(Fraction(nprod, dprod))
    print('wooooooah')

if __name__ == '__main__':
    prodinlowesterms()
