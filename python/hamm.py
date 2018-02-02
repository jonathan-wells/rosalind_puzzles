#!/usr/bin/env python3

def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(1 for i in range(len(s1)) if s1[i] != s2[i])

if __name__ == '__main__':
    s1 = 'GAGCCTACTAACGGGAT'
    s2 = 'CATCGTAATGACGGCCT'
    print(hamming(s1, s2))

