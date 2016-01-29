#!/usr/bin/env julia

using StatsBase

# Part1

"Returns the 5' -> 3' antisense strand of dna_string"
function complement_dna(dna_string)
    nucleotide_dict(x) = Dict("T"=>"A", "G"=>"C", "C"=>"G", "A"=>"T")[x]
    revd = reverse(dna_string)
    complement = replace(revd, r"([AGCT])", nucleotide_dict)
end

# Or a one liner:
# replace(reverse(chomp(readall("../input/puzzle3.txt"))), r"([AGCT])", x -> Dict("T"=>"A", "G"=>"C", "C"=>"G", "A"=>"T")[x])

# Part 2

"Returns dictionary of fastaIDs and associated DNA sequences."
function get_fastadict(fastafile)
    fastadict = Dict()
    infile = open(fastafile)
    id = ""
    for line in readlines(infile)
        if contains(line, ">")
            id = chomp(line)
            fastadict[id] = ""
        else
            fastadict[id] *= chomp(line)
        end
    end
    close(infile)
    return fastadict
end

"Given fasta sequences returns sequence with highest GC content."
function calc_maxgc_content(fastadict)
    maxgc = 0
    maxid = ""
    for id in keys(fastadict)
        props = proportionmap(split(fastadict[id], ""))
        gc = props["G"] + props["C"]
        if gc > maxgc
            maxgc = gc
            maxid = id
        end
    end
    return strip(maxid, '>'), 100*maxgc
end


dna = chomp(readall("../input/puzzle3a.txt"))
dna_complement = complement_dna(dna)
@printf("\n%-12s%s\n%-12s%s\n\n", "DNA:", dna, "COMPLEMENT:", dna_complement)

fd = get_fastadict("../input/puzzle3b.txt")
maxid, maxgc = calc_gc_content(fd)
@printf("ID:\t%s\nGC:\t%0.2f%%\n\n", maxid, maxgc)
