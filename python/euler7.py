#!/usr/bin/env python3

"""
Euler Puzzle 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10,001st prime number?
"""

def isprime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def count_primes(n):
    primes = []
    p = 1
    while primes.count(True) != n:
        p += 1
        primes.append(isprime(p))
    print(p)

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
    print(primes)
    print(len(primes))
    print(primes[0])
    print(primes[10000])


if __name__ == '__main__':
    prime_sieve(1000000)
