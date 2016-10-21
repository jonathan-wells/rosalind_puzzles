#!/usr/bin/env python3

import numpy as np


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

    def strip(self, i, j):
        return self.perm[i:j+1]

    def isincreasing(i, j):
        permstrip = self.strip(i, j)
        if max(permstrip) > min(permstrip):
            return True
        else:
            return False

    def bpdiff(self, other):
        return self.breakpoints - other.breakpoints

    def reversal(self, i, j):
        return self.perm[:i] + self.perm[i:j+1][::-1] + self.perm[j+1:]

    def __iter__(self):
        for i in self.perm:
            yield i

    def __len__(self):
        return len(self.perm)

    def __repr__(self):
        return ' '.join([str(i) for i in self.perm])


class PermutationPair(object):
    def __init__(self, pair):
        assert len(pair[0]) == len(pair[1])
        self.plen = len(pair[0])
        self.s1, self.s2 = Permutation(pair[0]), Permutation(pair[1])
        self.sigma, self.tau = self._relabel_pair()
        self.upper, self.lower = self._calc_bounds()
        self.current_best = self.greedy_dist()

    def _relabel_pair(self):
        mapping = {val: i+1 for (i, val) in enumerate(self.s1)}
        sigma = Permutation([mapping[val] for val in self.s1])
        tau = Permutation([mapping[val] for val in self.s2])
        return sigma, tau

    def _calc_bounds(self):
        upper = len(self.s1) - 1
        lower = 2
        return upper, lower

    def breakpointdiff(self, i, j):
        perm = Permutation(self.tau.reversal(i, j))
        return self.tau.bpdiff(perm)

    def greedy_dist(self):
        distance = 0
        old_tau = self.tau
        while self.tau.breakpoints != 0:
            dmat = np.zeros((self.plen, self.plen), int)
            best_bpdiff = 0
            i0, j0 = 0, 0
            for i in range(self.plen):
                for j in range(self.plen):
                    if i >= j:
                        continue
                    dmat[i][j] = self.breakpointdiff(i, j)
                    if dmat[i][j] > best_bpdiff:
                        best_bpdiff = dmat[i][j]
                        i0, j0 = i, j
            self.tau = Permutation(self.tau.reversal(i0, j0))
            distance += 1
        self.tau = old_tau
        return distance

################################################################################
## Graph structure for DFS
################################################################################

class Node(object):
    def __init__(self, name, parent, children=[]):
        self.name = name
        self.parent = parent
        self.children = children

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def add_node(self, name, parent):
        node = Node(name, parent)
        self.nodes.append(name, parent)
        self.edges.append((name, parent))


################################################################################
## Reversal distance algorithms
################################################################################

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

def exact_reversal_distance(seqpair):
    tree = Graph()
    pair = PermutationPair(seqpair)
    ubound = pair.current_best
    best = ubound
    dmat = np.zeros((pair.plen, pair.plen))
    best_bpdiff = 0
    i0, j0 = 0, 0
    for i in range(self.plen):
        for j in range(self.plen):
            if i >= j:
                continue
            dmat[i][j] = self.breakpointdiff(i, j)
            if dmat[i][j] > best_bpdiff:
                best_bpdiff = dmat[i][j]
                tree.add_node('', )
    self.tau = Permutation(self.tau.reversal(i0, j0))






if __name__ == '__main__':
    seqpairs = read_seqpairs('test.txt')
    exact_reversal_distance(seqpairs[1])
