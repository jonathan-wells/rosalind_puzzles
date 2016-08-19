#!/usr/bin/env julia


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


# tot_pcount = 0
# for window in 4:12
#     tot_pcount += find_palindromes("TCAATGCATGCGGGTCTATATGCAT", window)
# end
# println(tot_pcount)
# find_palindromes("TCAATGCATGCGGGTCTATATGCAT", 4)

function palindromedp(dnastring)
    (s1, s2) = (dnastring, reverse(complement_dna(dnastring)))
    matrix = zeros(Int, length(s1)+1, length(s2)+1)
    for i in 2:length(s1)
        for j in 2:length(s2)
            if s1[i-1] == s2[j-1]
                matrix[i, j] = matrix[i-1, j-1] + 1
            end
        end
    end
    longest = ""
    maxnum = 0
    startcoords = (1, 1)
    for i in 2:length(s1)
        for j in 2:length(s2)
            if matrix[i, j] > maxnum
                maxnum = matrix[i, j]
                startcoords = i, j
            end
        end
    end
    println(maxnum)
    println(startcoords)
    println(matrix)
end
# ACTGCGTAGCGATAACATCGCATGCGATAGC
palindromedp("ACTGCGTAGCGATATATAACGC")
