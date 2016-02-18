#!/usr/bin/env julia

function expected_dominant_offspring(genotype_counts::Vector)
    offspring_weights = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    expected = 2.0*sum(genotype_counts .* offspring_weights)
end


function fibonacci(n, k)
    if n == 1
        return 1
    elseif n == 2
        return 1
    else
        return fibonacci(n - 1, k) + k*fibonacci(n - 2, k)
    end
end

println(fibonacci(10, 3))

e = expected_dominant_offspring([18298.0, 16401.0, 17069.0, 18484.0,
                                18316.0, 16402.0])
println(e)
