#!/usr/bin/env python3

import numpy as np
from collections import OrderedDict

def read_file(filename):
    seqs = OrderedDict()
    with open(filename) as infile:
        for line in infile:
            if '>' in line:
                key = line.strip()
                seqs[key] = ''
            else:
                seqs[key] += line.strip()
    return seqs

def levenshtein_distance(s1, s2):
    """Shameless copy of Wikipedia Levenshtein distance page."""
    m, n = len(s1) + 1, len(s2) + 1
    mat = np.zeros((m, n), int)
    # Adds the extra indels/subs needed for prefix of diff length strings.
    mat[:, 0] = range(m)
    mat[0, :] = range(n)
    # pick best option of insertion, deletion or substitution where appropriate.
    for i, c1 in enumerate(s1, 1):
        for j, c2 in enumerate(s2, 1):
            sub_cost = int(bool(c1 != c2))  # Neat trick: if diff sc = True = 1
            mat[i][j] = min(mat[i-1, j-1] + sub_cost,
                            mat[i-1, j] + 1,
                            mat[i, j-1] + 1)
    return mat[m-1][n-1]

if __name__ == '__main__':
    seqs = read_file('../data/rosalind_edta.txt')
    ldist = levenshtein_distance(*seqs.values())
    print(ldist)
