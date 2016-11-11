#!/usr/bin/env python3

import numpy as np

def read_file(filename):
    seqs = {}
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
    for i in range(1, m):
        mat[i][0] = i
    for j in range(1, n):
        mat[0][j] = j
    # pick best option of insertion, deletion or substitution where appropriate.
    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]:
                sub_cost = 0
            else:
                sub_cost = 1
            mat[i][j] = min(mat[i-1][j-1] + sub_cost,
                            mat[i-1][j] + 1,
                            mat[i][j-1] + 1)
    return mat[m-1][n-1]

if __name__ == '__main__':
    seqs = read_file('../data/rosalind_edit.txt')
    ldist = levenshtein_distance(*seqs.values())
    print(ldist)
