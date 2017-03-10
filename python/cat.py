#!/usr/bin/env python3

import numpy as np

def readseq(filename):
    label, seq = [i.strip() for i in open(filename).readlines()]
    return seq

def correct_subgraphs(seq):
    pass

def catalan(n):
    n = int(n)
    if n <= 1:
        mem = np.zeros((2, 2))
    else:
        mem = np.zeros((n + 1, n + 1))
    mem[0, 1], mem[1, 1] = 1, 1
    cat = lambda i: sum(mem[i])
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            mem[i, j] = cat(j - 1)*cat(i - j)
    return cat(n)

if __name__ == '__main__':
    seq = readseq('test.txt')
    correct_subgraphs(seq)
    print(catalan(4))
