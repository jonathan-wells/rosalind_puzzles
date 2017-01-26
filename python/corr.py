#!/usr/bin/env python3

from collections import defaultdict
import numpy as np

def read_fasta(filename):
    seqs = defaultdict(str)
    with open(filename) as infile:
        for line in infile:
            if '>' in line:
                key = line.strip()
            else:
                seqs[key] += line.strip()
    return seqs

def hamming(s1, s2):
    return sum(i[0] != i[1] for i in zip(s1, s2))

def check_seqs(seqs):
    seqs = list(seqs.values())
    rev = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    revcomp = lambda s: ''.join([rev[c] for c in s[::-1]])
    seqcounts = {s: seqs.count(s) + seqs.count(revcomp(s)) for s in seqs}
    correct = [s for s in seqs if seqcounts[s] >= 2]
    incorrect = [s for s in seqs if seqcounts[s] < 2]
    corrections = []
    for s1 in incorrect:
        for s2 in correct:
            if hamming(s1, s2) == 1:
                corrections.append((s1, s2))
            elif hamming(s1, revcomp(s2)) == 1:
                corrections.append((s1, revcomp(s2)))
    return sorted(set(corrections))

def format_corrections(corrections):
    for corr in corrections:
        print(corr[0]+'->'+corr[1])

def main():
    seqs = read_fasta('../data/rosalind_corr.txt')
    corrections = check_seqs(seqs)
    format_corrections(corrections)

if __name__ == '__main__':
    main()
