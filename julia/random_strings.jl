#!/usr/bin/env julia

using StatsBase

function prob_random_string(dnastring::AbstractString, gc::Float64)
    nucprobs = Dict("A" => (1 - gc)/2, "C" => gc/2,
                    "T" => (1 - gc)/2, "G" => gc/2)
    splitstring = split(dnastring, "")
    stringprob::Float64 = sum([log(10, nucprobs[n]) for n in splitstring])
    return stringprob
end

function prob_random_string(dnastring::AbstractString, gc::Array{Float64})
    stringprob::Array{Float64} = [prob_random_string(dnastring, x) for x in gc]
    return stringprob
end

function main(filename)
    data = open(readlines, filename)
    dnastring = strip(data[1])
    gc_cont::Array{Float64} = [parse(Float64, i) for i in split(data[2], " ")]
    probs = prob_random_string(dnastring, gc_cont)
    println(join(probs, "\t"))
end

main(ARGS[1])
