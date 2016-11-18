#!/usr/bin/env python3

"""Module description here."""

import sys
import numpy as np
import edit

def needleman_wunsch(seq1, seq2):
    """"Needleman-Wunsch algorithm for global sequence alignment.

    Arguments:
        seq1, seq2 - sequences of interest
    Returns:
        fmat - scoring matrix
        pmat - pointer matrix describing construction of fmat
    """
    mdim, ndim = len(seq1) + 1, len(seq2) + 1
    # Initialise score (fmat) and pointer (pmat) matrices
    fmat = np.zeros((mdim, ndim), int)
    pmat = np.zeros((mdim, ndim), int)
    fmat[:, 0] = range(0, -mdim, -1)
    fmat[0, :] = range(0, -ndim, -1)
    # Set match/mismatch and indel penalties
    indel_pen = 1
    mismatch_pen = lambda x: bool(x[0] != x[1])
    for i, char1 in enumerate(seq1, 1):
        for j, char2 in enumerate(seq2, 1):
            # Compute scoring matrix
            match = fmat[i-1, j-1] - mismatch_pen((char1, char2))
            indeli = fmat[i-1, j] - indel_pen
            indelj = fmat[i, j-1] - indel_pen
            fmat[i, j] = max(match, indeli, indelj)
            # Compute pointer matrix
            if fmat[i, j] == indeli:
                pmat[i, j] = 1
            elif fmat[i, j] == match:
                pmat[i, j] = 2
            elif fmat[i, j] == indelj:
                pmat[i, j] = 3
    return fmat, pmat

def traceback(seq1, seq2, pmat):
    """Given a pointer matrix, generate alignment strings."""
    ali1, ali2 = '', ''
    dims = pmat.shape
    i, j = dims[0] - 1, dims[1] - 1
    while i > 0 or j > 0:
        if pmat[i, j] == 1:
            i -= 1
            ali1 += seq1[i]
            ali2 += '-'
        elif pmat[i, j] == 2:
            i -= 1
            j -= 1
            ali1 += seq1[i]
            ali2 += seq2[j]
        elif pmat[i, j] == 3:
            j -= 1
            ali1 += '-'
            ali2 += seq2[j]
    return ali1[::-1], ali2[::-1]

def hamming(seq1, seq2):
    """Return Hamming distance between two strings."""
    return sum(bool(x != y) for (x, y) in zip(seq1, seq2))

def global_align(seq1, seq2):
    """Use Needleman-Wunsh algorithm to globally align two sequences."""
    pmat = needleman_wunsch(seq1, seq2)[1]
    ali1, ali2 = traceback(seq1, seq2, pmat)
    dist = hamming(ali1, ali2)
    return ali1, ali2, dist

def main():
    """Run main on main."""
    seqs = edit.read_file(sys.argv[1])
    seq1, seq2 = [*seqs.values()][:2]
    ali1, ali2, dist = global_align(seq1, seq2)
    print(dist)
    print(ali1)
    print(ali2)

if __name__ == '__main__':
    main()
