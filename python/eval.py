#!/usr/bin/env python3

def read_data(filename):
    with open(filename) as infile:
        n = int(infile.readline().strip())
        s = infile.readline().strip()
        a = [float(gc) for gc in infile.readline().strip().split()]
    return n, s, a

def calc_string_prob(s, gc):
    """Calculate probability of generating s under given gc content."""
    nuc_probs = {'A': (1-gc)/2, 'C': gc/2, 'T':(1-gc)/2, 'G': gc/2}
    pstring = 1
    for nuc in s:
        pstring *= nuc_probs[nuc]
    return pstring

def expected_in_string(n, s, gc):
    """For a string of length n, return expected number of s-matches."""
    num_substrings = n + 1 - len(s)
    pstring = calc_string_prob(s, gc)
    expected = pstring*num_substrings
    return expected

def calc_barray(n, s, a):
    barray = []
    for gc in a:
        expected = expected_in_string(n, s, gc)
        barray.append(round(expected, 3))
    return barray

if __name__ == '__main__':
    n, s, a = read_data('../data/rosalind_eval.txt')
    barray = calc_barray(n, s, a)
    print(' '.join([str(i) for i in barray]))
