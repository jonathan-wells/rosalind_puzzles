#!/usr/bin/env python3

import sys
from math import factorial

def nsubsets(n):
    return 2**n

## Broken way using the sum of binomial coefficients - fails because of
## floating point arithmetic issues in math.factorial

def combinations(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

def nsubsets_alt(n):
    return sum(combinations(n, k) for k in range(0, n + 1))

def main(n):
    print(int(nsubsets(n)%1e6))

if __name__ == '__main__':
    main(int(sys.argv[1]))
