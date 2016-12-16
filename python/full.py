#!/usr/bin/env python3

import spec
import math

def load_data(filename):
    with open(filename) as infile:
        peptidemass = float(infile.readline())
        ionmasses = [float(m) for m in infile]
    return peptidemass, ionmasses

def pair_ions(peptidemass, ionmasses):
    npairs = int(len(ionmasses)/2)
    pairs = []
    while len(pairs) < npairs:
        mn, mx = min(ionmasses), max(ionmasses)
        pairs.append((mn, mx))
        ionmasses.remove(mn)
        ionmasses.remove(mx)
    pairs = sorted(pairs, key=lambda x: x[0])
    return pairs

def isresidue(obs, resmasses, tol):
    for ex in resmasses:
        if abs(ex - obs) <= tol:
            return True
    return False

def calc_peptide(pairs, error_tol=0.1):
    resmasses = spec.load_monoisotopic_masses()
    peptide_length = len(pairs) - 1
    i = 1
    while i < peptide_length:
        diff = pairs[i][0] - pairs[i-1][0]
        if isresidue(diff, resmasses, error_tol):
            i += 1
        else:  # Flip current pair and re-sort remaining
            pairs[i] = pairs[i][::-1]
            pairs[i:] = sorted(pairs[i:], key=lambda x: x[0])
    spectrum = [i[0] for i in pairs]
    print(spec.calc_peptide(spectrum, resmasses))

if __name__ == '__main__':
    pm, im = load_data('../data/rosalind_full.txt')
    pairs = pair_ions(pm, im)
    calc_peptide(pairs)
