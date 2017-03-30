#!/usr/bin/env python3

import numpy as np

"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143?
"""

def isprime(x):
    for i in range(2, int(np.floor(x**0.5))+1):
        if x%i == 0:
            return False
    return True

def prime_sieve(n):
    primes = list(range(2, n+1))
    for i, val in enumerate(primes):
        if primes[i] == 0:
            continue
        else:
            j = i + val
            while j < len(primes):
                primes[j] = 0
                j += val
    primes = [p for p in primes if p]
    return primes

def prime_factor(n=13195):
    factors = []
    curr = n
    for i in range(2, int(np.floor(n**0.5))+1):
        if curr%i == 0:
            factors.append(i)
            curr /= i
    factors.append(int(curr))
    factors = [i for i in factors if isprime(i)]
    return factors

class Test(object):
    def __init__(self):
        self.length = 10

    def __str__(self):
        return str(self.length)

if __name__ == '__main__':
    a = prime_factor(600851475143)
#     b = prime_factor(2*4*6*8*3*5)
#     c = prime_factor(17)
    print(a)
#     print(b)
#     print(c)

    # print('hello')
    test = Test()
    print(str(test))
