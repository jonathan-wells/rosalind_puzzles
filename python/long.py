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

def check_overlap(s1, s2, threshold=0.5):
    threshold = int(np.ceil(len(max(s1, s2, key=len))*threshold))
    overlaps = []
    for i in range(threshold, len(s1)):
        if s1[:i] == s2[-i:]:
            overlaps.append((i, 1))
    for i in range(threshold, len(s2)):
        if s2[:i] == s1[-i:]:
            overlaps.append((i, 2))
    if len(overlaps) == 0:
        return None
    else:
        return max(overlaps, key=lambda x: x[0])

def sort_seqs(seqs):
    seqs = sorted(seqs)
    seqmatches = {}
    for i, s1 in enumerate(seqs):
        for j, s2 in enumerate(seqs):
            if i <= j:
                continue
            ov = check_overlap(s1, s2)
            if ov and ov[1] == 1:
                seqmatches[s1] = ov[0], s2
            elif ov and ov[1] == 2:
                seqmatches[s2] = ov[0], s1
    joined = list(set(seqs) - set(seqmatches))[0]
    seqmatches = {v[1]: (k, v[0]) for k, v in seqmatches.items()}
    cur = seqmatches[joined]
    while seqmatches.get(cur[0], None):
        joined += cur[0][cur[1]:]
        cur = seqmatches[cur[0]]
    joined += cur[0][cur[1]:]
    print(joined)

if __name__ == '__main__':
    seqs = read_fasta('../data/rosalind_long.txt')
    seqs = list(seqs.values())
    sort_seqs(seqs)
