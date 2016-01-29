#!/usr/bin/env julia

using StatsBase

"Returns nucleotide proportions of DNA or RNA sequence."
function count_nucleotides(nt_string)
    splitstring = split(nt_string, "")
    nt_map = countmap(splitstring)
    freq_map = proportionmap(splitstring)
    println("NT\tCount\tProportion")
    for nt in keys(nt_map)
        @printf("%s:\t%d\t%0.2f %%\n", nt, nt_map[nt], freq_map[nt] * 100)
    end
end

"Transcribes DNA string."
function transcribe(nt_string, reverse = false)
    println(nt_string)
    for nt in nt_string
        if nt == 'T'
            print('*')
        else
            print('|')
        end
    end
    println()
    transcription_map = Dict("T" => "U", "G" => "G",
                             "C" => "C", "A" => "A")
    if reverse
        transcription_map["U"] = "T"
    end
    splitstring = split(nt_string, "")
    mapdict(nt) = transcription_map[nt]
    transcript = join(map(mapdict, splitstring), "")
    println(transcript)
end

println()
count_nucleotides("AGCTTTTCATTCTGACTGCAACGGGCAAT")
println()
transcribe("GATGGAACTTGACTACGTAAATT")
println()