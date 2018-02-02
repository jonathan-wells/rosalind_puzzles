#!/usr/bin/env python3

import re
import requests

def fetch_sequence(uniprot_id):
    """Returns protein sequence from UniProt server."""
    baseurl = 'http://www.uniprot.org/uniprot/'
    fasta = requests.get(f'{baseurl}{uniprot_id}.fasta').text
    fasta = fasta.strip().split('\n')
    uid, seq = fasta[0], ''.join(fasta[1:])
    return uid, seq

def find_motif_locs(pattern, seq):
    """Returns list of motif start sites, indexed from 1."""
    hits = re.finditer(pattern, seq)
    if hits:
        return [str(i.span()[0] + 1) for i in hits]

def read_ids(filename):
    """Returns list of UniProt accession ids from input file."""
    with open(filename) as infile:
        ids = [line.strip() for line in infile]
    return ids

def main():
    """Print protein ids and corresponding locations of glycosylation motifs."""
    ids = read_ids('../data/rosalind_mprt.txt')
    # lookahead r'(?=(pattern))' accounts for overlapping motifs
    glycosylation = re.compile('(?=(N[^P][ST][^P]))')
    for uid in ids:
        _, seq = fetch_sequence(uid)
        locs = find_motif_locs(glycosylation, seq)
        if locs:
            print(uid)
            print(' '.join(locs))

if __name__ == '__main__':
    main()
