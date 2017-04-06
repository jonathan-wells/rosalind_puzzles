#!/usr/bin/env python3

import math
import numpy as np

def firstndigits(ndigits, numbers):
    bufferdigits = int(np.ceil(math.log(len(numberlist))))
    reqnumbers = [int(i[:ndigits + bufferdigits + 1]) for i in numberlist]
    return str(sum(reqnumbers))[:ndigits + 1]


if __name__ == '__main__':
    with open('../data/euler13.dat') as infile:
        numberlist = infile.readlines()
    print(sum(int(i) for i in numberlist))
    print(firstndigits(10, numberlist))
