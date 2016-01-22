#!/usr/bin/env julia

using Distances

"Returns hamming distance between 2 strings"
function jhamming(s1, s2)
    # length(s1) != length(s2) && error("Length of strings must be equal")
    count = 0
    for i in zip(split(s1, ""), split(s2, ""))
        if length(Set(i)) == 2
            count += 1
        end
    end
    return count
end

s1 = "GAGCCTACTAACGGGATGAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCTGAGCCTACTAACGGGAT"
@time jhamming(s1, s2)
@time hamming(split(s1, ""), split(s2, ""))
