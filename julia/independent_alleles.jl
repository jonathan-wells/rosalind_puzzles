#!/usr/bin/env julia

function prob_double_het(k::BigInt, n::BigInt, p::Float64)
    prob = 0
    trials = 2^k
    for r in n:trials
        prob += binomial(trials, r)*p^r*(p-1.0)^(trials - r)
    end
    println(prob)
end

prob_double_het(BigInt(7), BigInt(37), 0.25)