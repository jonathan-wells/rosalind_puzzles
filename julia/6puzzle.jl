#!/usr/bin/env julia

"Return expected number of pairs "
function expected_dominant_offspring(parent_genotypes::Vector,
                                     num_offspring::Float64)
    offspring_weights = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    return num_offspring*sum(parent_genotypes.*offspring_weights)
end


"Given k pairs of offspring, return number of live pairs after n months."
function fibonacci(n, k)
    if n > 2
        return fibonacci(n - 1, k) + k*fibonacci(n - 2, k)
    else
        return 1
    end
end

println(@time fibonacci(45, 3))

# Sweet as
fibonacci(n, k) = n > 2  ? fibonacci(n-1, k) + k*fibonacci(n-2, k) : 1

println(@time fibonacci(45, 3))

parent_counts = [18298.0, 16401.0, 17069.0, 18484.0, 18316.0, 16402.0]
expected = expected_dominant_offspring(parent_counts, 3.0)
println(expected)
