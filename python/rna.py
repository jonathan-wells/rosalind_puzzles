#!/usr/bin/env python3

def transcribe(filename):
    """Converts DNA sequence from input file into equivalent RNA string."""
    with open(filename) as infile:
        rna_string = infile.read().strip()
    print(rna_string.replace('T', 'U'))

if __name__ == '__main__':
    transcribe('../data/rosalind_rna.txt')
