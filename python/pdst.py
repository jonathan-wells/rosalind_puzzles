#!/usr/bin/env python3

import numpy as np
from collections import OrderedDict

def read_fasta(filename):
    fastaseqs = OrderedDict()
    with open(filename) as infile:
        for line in infile:
            if '>' in line:
                label = line.strip()
                fastaseqs[label] = ''
            else:
                fastaseqs[label] += line.strip()
    return list(fastaseqs.values())

def pdistance(s1, s2):
    n, m = len(s1), len(s2)
    assert n == m
    diff = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff += 1
    return diff/n

def calc_dmatrix(filename):
    seqs = read_fasta(filename)
    n = len(seqs)
    dmatrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dmatrix[i][j] = pdistance(seqs[i], seqs[j])
    return dmatrix

def prettyprint_dmatrix(filename):
    n, m = dmatrix.shape
    for i in range(n):
        for j in range(n):
            print('{0:.5f}'.format(dmatrix[i][j]), end=' ')
        print()

if __name__ == '__main__':
    dmatrix = calc_dmatrix('../data/rosalind_pdst.txt')
    prettyprint_dmatrix(dmatrix)
