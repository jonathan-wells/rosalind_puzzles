#!/usr/bin/env python3

from collections import defaultdict
import re
import sys
import numpy as np


class BLOSUM(object):

    def __init__(self, n):
        try:
            filename = f'../data/BLOSUM{n}.txt'
            infile = open(filename, 'r')
        except IOError:
            raise

        # Generate numpy array for BLOSUM matrix
        blosum = []
        for line in infile:
            if '#' in line:
                continue
            if re.match(r'\s+[A-Z].+', line):
                # dictionary of array indices for each amino acid
                self.amino = {aa: i for i, aa in enumerate(line.split())}
            else:
                blosum.append([int(i) for i in line.split()[1:]])
        infile.close()
        self.blosum = np.array(blosum)

    def __getitem__(self, pair):
        """Return match score for given pair of amino acids."""
        return self.blosum[self.amino[pair[0]], self.amino[pair[1]]]


class NeedlemanWunsch(object):
    """Needleman-Wunsch algorithm for global sequence alignment.

    Arguments:
        blosumnum - Variant of BLOSUM scoring matrix to be used.
        gapopen - Penalty for opening a new gap in the sequence.

    Methods:
        generate_matrices - Generates scoring and backtrace matrices.
        score - Return best score for two sequences.
    """


    def __init__(self, blosumnum=62, gapopen=-5):
        self.gapopen = gapopen
        self.blosum = BLOSUM(blosumnum)

    def generate_matrices(self, s1, s2):
        """Generate scoring matrix for given sequence and scoring system."""
        self.m, self.n = len(s1), len(s2)
        self.s1, self.s2 = s1, s2
        self.scoremat = np.zeros((self.m + 1, self.n + 1), int)

        # Initialise first row/column of scoremat matrix
        for i in range(1, self.m + 1):
            self.scoremat[i, 0] = self.scoremat[i - 1, 0] + self.gapopen
        for j in range(1, self.n + 1):
            self.scoremat[0, j] = self.scoremat[0, j - 1] + self.gapopen

        # Generate the rest
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                char1, char2 = self.s1[i - 1], self.s2[j - 1]
                matchscore = self.blosum[(char1, char2)]

                newcell = max(self.scoremat[i - 1, j] + self.gapopen,
                              self.scoremat[i, j - 1] + self.gapopen,
                              self.scoremat[i - 1, j - 1] + matchscore)
                self.scoremat[i, j] = newcell

    def score(self, s1, s2):
        try:
            return np.amax(self.scoremat)
        except AttributeError:
            self.generate_matrices(s1, s2)
            return np.amax(self.scoremat)       
    
    def __repr__(self):
        try:
            return str(self.scoremat)
        except:
            self.generate_matrices()
            return str(self.scoremat)

def main(filename):
    """Reads file and aligns sequences within."""
    seqs = defaultdict(str)
    with open(filename) as infile:
        for line in infile:
            if '>' in line:
                key = line.strip()
            else:
                seqs[key] += line.strip()
    assert len(seqs) == 2
    seqs = list(seqs.values())

    aligner = NeedlemanWunsch()
    # Actually, try except is bad because if you try to give it new seqs...
    print(aligner.score(seqs[0], seqs[1]))

if __name__ == '__main__':
    main(sys.argv[1])
