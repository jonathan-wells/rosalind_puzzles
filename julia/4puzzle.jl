#!/usr/bin/env julia


# Part 1
# function npermutations(n)
#     iterable = collect(1:n)
#     perms = [i for i in permutations(iterable)]
# end

# for i in npermutations(3)
#     println(i)
# end

# Part 3
"Returns the 5' -> 3' antisense strand of dna_string"
function complement_dna(dna_string)
    nucleotide_dict(x) = Dict("T"=>"A", "G"=>"C", "C"=>"G", "A"=>"T")[x]
    revd = reverse(dna_string)
    complement = replace(revd, r"([AGCT])", nucleotide_dict)
end

function chop_string(string, window)
    chopped_strings = []
    for i in 1 : (length(string) - window + 1)
        chopped = string[i:i + window - 1]
        push!(chopped_strings, chopped)
    end
    return chopped_strings
end

function find_palindromes(string, window)
    println(string)
    palindromes = [complement_dna(s) for s in chop_string(string, window)]
    pcount = 0
    for p in palindromes
        pattern =  Regex("$p")
        m = match(pattern, string)
        if m != nothing
            pcount += 1
            println(p)
            println(m.offset)
        end
    end
    return pcount
end


tot_pcount = 0
for window in 4:12
    tot_pcount += find_palindromes("TCAATGCATGCGGGTCTATATGCAT", window)
end
println(tot_pcount)
# find_palindromes("TCAATGCATGCGGGTCTATATGCAT", 4)
