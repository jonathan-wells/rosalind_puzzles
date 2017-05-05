#!/usr/bin/env python3

from math import factorial

def permute(iterable):
    iterable = sorted(iterable)
    n = len(iterable)
    nperms = factorial(n)
    count = 0
    while count < nperms:
        yield iterable
        j, k = 0, 0
        for i in range(n - 1):
            if iterable[i] < iterable[i + 1]:
                k = i
        for i in range(k, n):
            if iterable[k] < iterable[i]:
                j = i
        iterable[j], iterable[k] = iterable[k], iterable[j]
        iterable[k + 1:] = iterable[k + 1:][::-1]
        count += 1

def main():
    count = 0
    for i in permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        count += 1
        if count == 1000000:
            print(i)
            break

if __name__ == '__main__':
    main()
