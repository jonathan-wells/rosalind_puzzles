#!/usr/bin/env python3

def frequency(dna_string):
    """Calculate nucleotide frequencies in string of interest."""
    freqs = {c: 0 for c in dna_string}
    for c in dna_string:
        freqs[c] += 1
    return freqs

def string_prob(dna_string, gc):
    """Probability of getting dna_string under given background gc content."""
    freqs = frequency(dna_string)
    at, gc = (1.0 - gc)/2.0, gc/2.0
    prob = 1
    for key in freqs:
        if key == 'A' or key == 'T':
            prob *= at**freqs[key]
        elif key == 'G' or key == 'C':
            prob *= gc**freqs[key]
    return prob

def prob_in_ntrials(n, gc, dna_string):
    """"Probability of seeing string of interest in n trials with bg gc."""
    sprob = string_prob(dna_string, gc)
    # P(at least 1) = 1 - P(none)
    prob = 1.0 - (1.0 - sprob)**n
    return prob

if __name__ == '__main__':
    dna_string = 'AAGCACAAG'
    gc = 0.516450
    n = 87679
    print('{0:.3f}'.format(prob_in_ntrials(n, gc, dna_string)))
