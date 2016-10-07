#!/usr/bin/env python3

from math import factorial

def perfect_basepair_matchings(seq):
    au = len([x for x in seq if x == 'A'])
    cg = len([x for x in seq if x == 'C'])
    return factorial(au)*factorial(cg)

if __name__ == '__main__':
    m = perfect_basepair_matchings('AGCCUAUGACGUUCAUGUCGCGGUGACUCAUGGUUCCAACCAACGGAAUUCUGGCACACCUGCCUAGGAGGG')
    print(m)
