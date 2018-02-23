#!/usr/bin/env python3

import re

def read_fasta(filename):
    seq = ''
    with open(filename) as infile:
        key = infile.readline().strip()
        for line in infile:
            seq += line.strip()
    return key, seq

def reverse_complement(seq):
    basepairing = {'A': 'T',
                   'T': 'A',
                   'G': 'C',
                   'C': 'G'}
    rev = ''
    for char in seq[::-1]:
        rev += basepairing[char]
    return rev

def find_reverse_palindrome(seq):
    locs = set()
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j - i < 4 or j - i > 12:
                continue
            if seq[i:j] == reverse_complement(seq[i:j]):
                occurrences = re.finditer(seq[i:j], seq)
                for k in occurrences:
                    locs.add((k.start() + 1, len(seq[i:j])))
    for pair in sorted(locs):
        print(pair[0], pair[1])

if __name__ == '__main__':
    key, seq = read_fasta('../data/rosalind_revp.txt')
    find_reverse_palindrome(seq)
