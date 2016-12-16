#!/usr/bin/env python

import sys
from itertools import permutations

def read_file(filename):
    with open(filename) as infile:
        chars = infile.readline().split()
        kmers = int(infile.readline().strip())
    return chars, kmers

def gen_strings(chars, kmers):
    kstring = ''.join([c*kmers for c in chars])
    perms = set(p for i in range(1, kmers+1) for p in permutations(kstring, i))
    return perms

def lexicographic_sort(strings, alphabet):
    order = {alphabet[i]: i for i in range(len(alphabet))}
    lexsorted = sorted(strings, key=lambda x: tuple(order[c] for c in x))
    return lexsorted

def main(filename):
    chars, kmers = read_file(filename)
    permuted = gen_strings(chars, kmers)
    lexsorted = lexicographic_sort(permuted, chars)
    for tup in lexsorted:
        print(''.join(tup))

if __name__ == '__main__':
    main(sys.argv[1])
