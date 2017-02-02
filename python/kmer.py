#!/usr/bin/env python3

import lexv
from itertools import permutations

def read_seq(filename):
    with open(filename) as infile:
        if '>' in infile.readline():
            return ''.join([i.strip() for i in infile])

def gen_kmers(seq, k):
    vals = ''.join([x*min(k, seq.count(x)) for x in set(seq)])
    kmers = set(''.join(i) for i in permutations(vals, k))
    return lexv.lexicographic_sort(kmers, 'ACGT')

def overlapping_count(string, seq):
    """Default count method does not count overlaps, so this fixes"""
    count = 0
    k = len(string)
    i = k
    # Good old sliding window
    while i <= len(seq):
        if seq[i - k:i] == string:
            count += 1
        i += 1
    return count

def ovcount(substring, string):
    """Faster version of above."""
    k, l = len(substring), len(string)
    return sum(1 for i in range(k, l) if string[i - k:i] == substring)

def gen_array(filename, k):
    """Pretty print space-separated array."""
    seq = read_seq(filename)
    kmers = gen_kmers(seq, k)
    for string in kmers:
        print(ovcount(string, seq), end=' ')

if __name__ == '__main__':
    gen_array('../data/rosalind_kmer.txt', 4)
