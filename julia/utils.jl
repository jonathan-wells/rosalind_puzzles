#!/usr/bin/env julia

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
