#!/usr/bin/env python3

import numpy as np

def longest_common_subsequence(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    mat = np.zeros((m, n), int)   # scores
    pmat = np.zeros((m, n), int)  # pointer
    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
                pmat[i][j] = 2
            else:
                left, up = mat[i-1][j], mat[i][j-1]
                mat[i][j] = max((left, up))
                if max((left, up)) == left:
                    pmat[i][j] = 1
                else:
                    pmat[i][j] = 3
    # traceback
    lcsq = ''
    i, j = np.unravel_index(mat.argmax(), mat.shape)
    while pmat[i][j] != 0:
        if pmat[i][j] == 1:
            i -= 1
        elif pmat[i][j] == 2:
            i -= 1
            j -= 1
            lcsq += s1[i]
        elif pmat[i][j] == 3:
            j -= 1
    return lcsq[::-1]

def shortest_common_superseq(s1, s2):
    lcsq = longest_common_subsequence(s1, s2)
    s1_missing, s2_missing = '', ''
    for i, char in enumerate(s):
        if lcsq_ind == len(lcsq) - 1:
            break
        if char == lcsq[lcsq_ind]:
            lcsq_ind += 1
        else:
            s1_missing += char
    print(s1_missing)



if __name__ == '__main__':
    s1, s2 = 'ATCTGAT', 'TGCATA'
    # longest_common_subsequence(s1, s2)
    shortest_common_superseq(s1, s2)
