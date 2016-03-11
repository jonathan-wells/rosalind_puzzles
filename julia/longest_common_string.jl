#!/usr/bin/env julia

include("utils.jl")

"Builds matrix of match/mismatch scores."
function build_lcsmatrix(seq1::ASCIIString, seq2::ASCIIString)
    m, n = length(seq1), length(seq2)
    lcsmatrix = zeros(Int, (m + 1, n + 1))
    for i in 2:m+1
        for j in 2:n+1
            if seq1[i-1] == seq2[j-1]
                lcsmatrix[i, j] = lcsmatrix[i-1, j-1] + 1
            end
        end
    end
    return lcsmatrix
end

"Performs traceback through lcsmatrix to build optimal common substring."
function traceback(seq1, seq2, lcsmatrix)
    substring = ""
    i, j = ind2sub(size(lcsmatrix), indmax(lcsmatrix))
    maxval = lcsmatrix[i, j]
    while lcsmatrix[i, j] != 0
        substring *= string(seq1[i-1])
        i, j = i-1, j-1
        # Reset as you go to allow later calculation of suboptimal strings.
        lcsmatrix[i+1, j+1] = 0
    end
    return reverse(substring), maxval
end

"Returns the set of all possible common substrings of seqs 1 and 2."
function all_substrings(seq1, seq2, minlen::Int=2)
    lcsmatrix = build_lcsmatrix(seq1, seq2)
    substrings = []
    currmax = Inf
    while currmax >= minlen
        substring, maxval = traceback(seq1, seq2, lcsmatrix)
        currmax = maxval
        # Generate all strings within and including optimal substring
        for start in 1:length(substring)
            for finish in start:length(substring)
                inner = substring[start:finish]
                length(inner) >= minlen && push!(substrings, inner)
            end
        end
    end
    return collect(Set(substrings))
end

"Given a set of sequences, returns the optimal common substring"
function multi_lcs(sequences, minlen)
    numseqs = length(sequences)
    candidates = all_substrings(sequences[1], sequences[2], minlen)
    sort!(candidates, by = x->length(x), rev=true)
    for substring in candidates
        matches = 0
        for seq in sequences
            if ismatch(Regex(substring), seq)
                matches += 1
            end
        end
        matches == numseqs && return substring
    end
end

function main(filename, minlen)
    sequences = collect(values(get_fastadict(filename)))
    lcs = multi_lcs(sequences, minlen)
    println(lcs)
end

main("../data/rosalind_lcsm.txt", 10)

