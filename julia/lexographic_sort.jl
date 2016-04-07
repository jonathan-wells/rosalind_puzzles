#!/usr/bin/env julia

using Iterators

function lexographic_sort(alphabet::Array, k::Int)
    order = [alphabet[i] => i for i in 1:length(alphabet)]
    kmerwords = collect(product([alphabet for i in 1:k]...))
    word = kmerwords[1]
    sort!(kmerwords, by = word->tuple([order[c] for c in word]...))
    for word in kmerwords
        println(join(word))
    end
end

lexographic_sort(["G", "W", "F", "Z", "V", "J", "U", "H"] , 3)
