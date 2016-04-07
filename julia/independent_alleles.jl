#!/usr/bin/env julia

function prob_double_het(k::BigInt, n::BigInt)
    prob = 0
    trials = 2^k
    for r in n:trials
        prob += binomial(trials, r)*0.25^r*0.75^(trials - r)
    end
    println(prob)
end

prob_double_het(BigInt(7), BigInt(37))