#!/usr/bin/env julia

function codonmap()
    codonfile = open("../data/codon_table.txt")
    codondata = [split(line, ' ') for line in readlines(codonfile)]
    codon = [pair[1] => chomp(pair[2]) for pair in codondata]
    return codon
end

function translate(mrna::AbstractString)
    codon = codonmap()
    triplet = 3
    protein = ""
    i, aa = 1, ""
    while aa != "Stop"
        protein *= aa
        aa = codon[mrna[i:i+2]]
        i += triplet
    end
    return protein
end

println(translate("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
