#!/usr/bin/env julia

using StatsBase

"Returns the 5' -> 3' antisense strand of dna_string"
function complement_dna(dna_string)
    nucleotide_dict(x) = Dict("T"=>"A", "G"=>"C", "C"=>"G", "A"=>"T")[x]
    revd = reverse(dna_string)
    complement = replace(revd, r"([AGCT])", nucleotide_dict)
end

# Or a one liner:
# replace(reverse(chomp(readall("../input/puzzle3.txt"))), r"([AGCT])", x -> Dict("T"=>"A", "G"=>"C", "C"=>"G", "A"=>"T")[x])

"Returns dictionary of fastaIDs and associated DNA sequences."
function get_fastadict(fastafile)
    # Open file and assert first line is correct format
    infile = open(fastafile)
    @assert contains(readline(infile), ">") "fasta format is incorrect"
    seekstart(infile)
    # Initialise and build fastadict
    fastadict = Dict()
    id = ""
    for line in readlines(infile)
        if contains(line, ">")
            id = chomp(line)
            fastadict[id] = ""
        else
            fastadict[id] *= chomp(line)  # Join julia strings with * not +
        end
    end
    close(infile)
    return fastadict
end

"Given fasta sequences returns sequence with highest GC content."
function calc_maxgc_content(fastadict::Dict)
    maxgc = 0.0
    maxid = ""
    for id in keys(fastadict)
        props = proportionmap(split(fastadict[id], ""))
        gc = props["G"] + props["C"]
        if gc > maxgc
            maxgc = gc
            maxid = id
        end
    end
    return strip(maxid, '>'), 100.0*maxgc
end

function main()
    # Part 1
    dna = chomp(readall("../data/puzzle3a.txt"))
    dna_complement = complement_dna(dna)
    @printf("%-12s%s\n%-12s%s\n\n", "DNA:", dna, "COMPLEMENT:", dna_complement)
    # Part 2
    fastadict = get_fastadict("../data/puzzle3b.txt")
    maxid, maxgc = calc_maxgc_content(fastadict)
    @printf("ID:\t%s\nGC:\t%0.2f%%\n", maxid, maxgc)
end

# main()

