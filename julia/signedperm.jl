#!/usr/bin/env julia

using Permutations

function signedperm(n)
    intset = Set(collect(-n:n))
    delete!(intset, 0)
    permset = Permutation(Array(intset))
    return permset
end

for pair in signedperm(5)
    println(pair[1], " ", pair[2])
end
