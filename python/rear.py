#!/usr/bin/env python3

import numpy as np
from collections import namedtuple

def read_seqpairs(filename):
    seqpairs = [[]]
    with open(filename) as infile:
        pairnum = 0
        for line in infile:
            if line == '\n':
                pairnum += 1
                seqpairs.append([])
            else:
                perm = [int(i) for i in line.strip().split()]
                seqpairs[pairnum].append(perm)
    return seqpairs


class Permutation(object):
    def __init__(self, perm):
        self.perm = perm
        self.n = len(perm)

    @property
    def breakpoints(self):
        bps = 0
        perm = [0] + self.perm + [self.n + 1]
        for i in range(self.n + 1):
            if abs(perm[i] - perm[i + 1]) != 1:
                bps += 1
        return bps


class PermutationPair(object):

    Label = namedtuple('Label', ['val', 'lab'])

    def __init__(self, pair):
        assert len(pair[0]) == len(pair[1])
        self.s1, self.s2 = Permutation(pair[0]), Permutation(pair[1])
        self.sigma, self.tau = self._relabel_seqpair(pair)
        self.sigma = Permutation([i.lab for i in self.sigma])
        self.tau = Permutation([i.lab for i in self.tau])

    def _relabel_seqpair(self, pair):
        pair[0] = [self.Label(val, lab+1) for (lab, val) in enumerate(pair[0])]
        mapping = dict(pair[0])
        pair[1] = [self.Label(key, mapping[key]) for key in pair[1]]
        return pair[0], pair[1]

if __name__ == '__main__':
    seqpairs = read_seqpairs('test.txt')
    pair = PermutationPair(seqpairs[1])
    print(pair.sigma.breakpoints)
