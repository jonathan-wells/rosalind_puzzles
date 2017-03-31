#!/usr/bin/env python3

"""
Problem 15 - Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# from scipy.special import binom
from math import factorial

def binomcoef(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n - k)))

def latticepaths(x, y):
    print(binomcoef(x + y, x))

if __name__ == '__main__':
    latticepaths(20, 20)
