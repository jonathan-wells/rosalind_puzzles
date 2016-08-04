#!/usr/bin/env julia

# Swaps values at positions i1 and i2 in an array
function swap!(a::Array, i1::Int, i2::Int)
    temp = a[i1]
    a[i1] = a[i2]
    a[i2] = temp
end

# Prints permutations, plus information about level in  recursion
function heaps_debugger(a::Array, n::Int=length(a))
    if n == 1
        println("a = ", a)
    else
        for i in 1:n
            println("n = ", n)
            println("i = ", i)
            heaps_debugger(a, n-1)
            if n%2 == 0
                swap!(a, i, n)
            else
                swap!(a, 1, n)
            end
        end
    end
end

# Utilises generator style function to produce permutations
function permutations(a::Array, n::Int=length(a))
    function _heaps(a::Array, n::Int)
        if n == 1
            produce(a)
        else
            for i in 1:n
                _heaps(a, n-1)
                n%2 == 0 ? swap!(a, i, n) : swap!(a, 1, n)
            end
        end
    end
    return @task _heaps(a, n)
end

function printperms(n::Int)
    out = []
    for p in permutations(collect(1:n))
        string = join(p, " ")
        push!(out, string)
    end
    println(length(out))
    for i in out
        println(i)
    end
end

printperms(6)
