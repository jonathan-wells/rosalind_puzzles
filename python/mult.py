#!/usr/bin/env python3

from collections import defaultdict
import numpy as np

def read_fasta(filename):
    fasta = defaultdict(str)
    with open(filename) as infile:
        for line in infile:
            if line[0] == '>':
                key = line.strip()
            else:
                fasta[key] += line.strip()
    return fasta

def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(bool(i != j) for i, j in zip(s1, s2))

def dp_multiple_align(seqs):
    dims = [len(seq) + 1 for seq in seqs]
    mat = np.zeros(dims, dtype=int)
    traceback = np.zeros(dims, dtype=int)
    # Initialise matrix
    for i in range(1, dims[0]):
        mat[i, 0] = mat[i-1, 0] - 1
        traceback[i, 0] = 1
    for j in range(1, dims[1]):
        mat[0, j] = mat[0, j-1] - 1
        traceback[0, j] = 2

    # Fill matrix
    for i in range(1, dims[0]):
        for j in range(1, dims[1]):
            insertion = mat[i-1, j] - 1
            deletion = mat[i, j-1] - 1
            match = mat[i-1, j-1] - hamming(seqs[0][i-1], seqs[1][j-1])
            mat[i, j] = max(insertion, deletion, match)
            if mat[i, j] == insertion:
                traceback[i, j] = 1
            elif mat[i, j] == deletion:
                traceback[i, j] = 2
            else:
                traceback[i, j] = 3
    
    # Traceback
    s1, s2 = seqs[0], seqs[1]
    i, j = len(s1), len(s2)
    ns1, ns2 = '', ''
    while traceback[i, j] != 0:
        if traceback[i, j] == 3:
            ns1 += s1[i-1]
            ns2 += s2[j-1]
            i -= 1
            j -= 1
        elif traceback[i, j] == 1:
            ns1 += s1[i-1]
            ns2 += '-'
            i -= 1
        elif traceback[i, j] == 2:
            ns1 += '-'
            ns2 += s2[j-1]
            j -= 1
    print(ns1[::-1])
    print(ns2[::-1])

if __name__ == '__main__':
    fasta = read_fasta('test.txt')
    seqs = list(fasta.values())
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i >= j:
                continue
            dp_multiple_align([seqs[i], seqs[j]])
