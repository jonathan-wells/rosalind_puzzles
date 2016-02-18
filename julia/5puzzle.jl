#!/usr/bin/env julia

include("3puzzle.jl")

"Return Probability of dominant offspring given population genotypes"
function mendelian_inheritance(k::Int, m::Int, n::Int)
    @assert k > 0; m > 0; n > 0
    population = Dict("XX" => k, "Xx" => m, "xx" => n)

    # Calculates conditional probability without replacement, P(A|B)
    function conditionalp(x, y)
        p(event, tot) = event/tot  # P(A)
        total = sum(values(population))
        if x == y
            prob = p(population[x], total) * p(population[y] - 1, total - 1)
        else
            prob = p(population[x], total) * p(population[y], total - 1)
        end
        return prob
    end

    # Dictionary of hermaphrodite couples
    couples = Dict()
    for p1 in keys(population)
        for p2 in keys(population)
            couples[(p1, p2)] = conditionalp(p1, p2)
        end
    end
    # Multiply P(pairing) * P(dominant offspring | pairing)
    for parents in keys(couples)
        if parents == ("Xx", "Xx")
            couples[parents] *= 0.75
        elseif parents == ("Xx", "xx") || parents == ("xx", "Xx")
            couples[parents] *= 0.5
        elseif parents == ("xx", "xx")
            couples[parents] *= 0
        end
    end
    return sum(values(couples))
end

"Calculates overlap graph O(k) for a dictionary of strings, given k"
function overlap_graph(strings::Dict, k::Int)
    overlap = Set()
    for key1 in keys(strings)
        for key2 in keys(strings)
            if key1 == key2
                continue
            end
            s = strings[key1]
            t = strings[key2]
            if s[(length(s) - k + 1):end] == t[1:k]
                push!(overlap, (strip(key1, '>'), strip(key2, '>')))
            end
        end
    end
    return overlap
end

"Pretty print output"
function main()
    # Part 1
    k, m, n = 250, 500, 250
    println("\nPart 1 - Mendelian Inheritance\n------")
    @printf("Given %d XX, %d Xx and %d xx:\n", k, m, n)
    p = mendelian_inheritance(k, m, n)
    @printf("P(dominant offpsring) = %f\n", p)
    # Part 2
    println("\nPart 2 - Overlap Graphs\n------")
    fastadict = get_fastadict("../data/rosalind_grph.txt")
    for edge in collect(overlap_graph(fastadict, 3))[1:10]
        @printf("%s\t%s\n", edge[1], edge[2])
    end
    println("...\n...\n")
end

main()
