#!/usr/bin/env julia

using Requests

function download_fasta(uniprotid)
    baseurl = "http://www.uniprot.org/uniprot/"
    url = join([baseurl, uniprotid, ".fasta"], "")
    data = split(readall(get(url)), "\n")
    name = data[1]
    sequence = chomp(join(data[2:end]))
    return name, sequence
end

function motif_search(motif::Regex, sequence::ASCIIString)
    start = 1
    motifindices = []
    lastind = endof(seq)
    while start != 0:-1
        start = search(sequence, motif, start[1]+1)
        start != 0:-1 ? push!(motifindices, start[1]) : return motifindices
    end
end

name, seq = download_fasta("B5ZC00")
indices = motif_search(Regex("N[^P][S|T][^P]"), seq)
println(name)
println(join(indices, "\t"))

# >>> >sp|B5ZC00|SYG_UREU1 Glycine--tRNA ligase OS=Ureaplasma urealyticum serovar 10 (strain ATCC 33699 / Western) GN=glyQS PE=3 SV=1
# >>> 85  118 142 306 395