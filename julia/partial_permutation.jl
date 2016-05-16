#!/usr/bin/env julia

function partialperm(n, k)
    factorial(n)/(factorial(n - k))
end

function partialperm_modulo(n, k, m)
    numerator = n
    denominator = (n - k)
    for i in 1:n-1
        numerator *= (numerator - i)%m
    end
    for i in 1:n-k-1
        denominator *= (denominator - i)%m
    end

    # println(numerator/denominator)%m
end

println(partialperm(4, 3)%100)

partialperm_modulo(4, 3, 100)