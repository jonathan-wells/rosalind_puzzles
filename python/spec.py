#!/usr/bin/env python3

import sys

def load_prefix_spectrum(filename):
    """Return simplified prefix spectrum for peptide of interest."""
    with open(filename) as infile:
        spectrum = [float(i.strip()) for i in infile]
    return spectrum

def load_monoisotopic_masses():
    """Return dictionary of precomputed monoisotropic residue masses."""
    monoisotopic_masses = {}
    with open('../data/monoistopic_mass_table.txt') as infile:
        for line in infile:
            line = line.split()
            monoisotopic_masses[float(line[1])] = line[0]
    return monoisotopic_masses

def calc_peptide(spectrum, mi_masses):
    """Return optimal peptide based on LMS estimate of residue."""
    # Calculate residue masses from adjacent prefix weights.
    observed_masses = []
    for i in range(len(spectrum) - 1):
        mass = spectrum[i+1] - spectrum[i]
        observed_masses.append(mass)
    # Calculate optimal peptide.
    peptide = ''
    for obs in observed_masses:
        # Minimise squared distance between observed and expected mass.
        mass_errors = {mi_masses[ex]: (obs - ex)**2 for ex in mi_masses}
        peptide += min(mass_errors, key = lambda x: mass_errors[x])
    return peptide

def main():
    spectrum = load_prefix_spectrum(sys.argv[1])
    masses = load_monoisotopic_masses()
    peptide = calc_peptide(spectrum, masses)
    print(peptide)

if __name__ == '__main__':
    main()
