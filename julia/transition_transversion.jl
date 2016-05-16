#!/usr/bin/env julia

function hamming(s1, s2)
    @assert length(s1) == length(s2)
    count = 0
    for i in 1:length(s1)
        s1[i] == s2[i] ? count += 1 : nothing
    end
    return count
end

function transitions(s1, s2)
    transition = Dict("A" => "G", "G" => "A", "C" => "T", "T" => "C")
    # Create new string with all possible transitions from sequence 1
    r1 = replace(s1, r"A|C|G|T", x->transition[x])
    return hamming(r1, s2)
end

function transversions(s1, s2)
    # Need 2 dictionaries to account for each way of transverting a base
    vert_transversion = Dict("A" => "C", "C" => "A", "G" => "T", "T" => "G")
    diag_transversion = Dict("A" => "T", "T" => "A", "C" => "G", "G" => "C")
    r1 = replace(s1, r"A|C|G|T", x->vert_transversion[x])
    r2 = replace(s1, r"A|C|G|T", x->diag_transversion[x])
    return hamming(r1, s2) + hamming(r2, s2)
end

function main()
    # Open and read fasta file
    filename = ARGS[1]
    infile = open(readall, filename)
    data = split(infile, "\n>")
    getseq(i) = join(split(data[i], "\n")[2:end], "")
    s1, s2 = getseq(1), getseq(2)
    # Calculate and print ratio
    println(transitions(s1, s2)/transversions(s1, s2))
end

main()
