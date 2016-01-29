#!/usr/bin/env python3

def hamming(str1, str2):
    return len([h for h in zip(str1, str2) if len(set(h)) == 2])

str1 = 'GAGCCTACTAACGGGATGAGCCTACTAACGGGAT'
str2 = 'CATCGTAATGACGGCCTGAGCCTACTAACGGGAT'
h = hamming(str1, str2)
print(h)