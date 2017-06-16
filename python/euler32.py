#!/usr/bin/env python3

from itertools import permutations

def splitnum(n):
    numbers = set()
    while n:
        digit = n % 10
        n //= 10
        numbers.add(digit)
    return numbers

def getlimits(n):
    newlist = []
    numbers = sorted(splitnum(n))
    for p in permutations(numbers[1:], 4):
        if len(splitnum(numbers[0] * int(''.join(str(i) for i in p)))) > 5:
            print(numbers[0], p, numbers[0] * int(''.join(str(i) for i in p)))
    # numbers[0] * numbers[1:4]

if __name__ == '__main__':
    getlimits(123456789)
