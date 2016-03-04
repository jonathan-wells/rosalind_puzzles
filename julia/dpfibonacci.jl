#!/usr/bin/env julia

function dpfibonacci(n, life)
    life += 1
    fibmem = [1, 1]
    for i in 3:n
        if n <= 2
            return fibmem[n]
        elseif i < life
            push!(fibmem, fibmem[i-1] + fibmem[i-2])
        elseif i == life
            push!(fibmem, fibmem[i-1] + fibmem[i-2] - 1)
        elseif i > life
            push!(fibmem, fibmem[i-1] + fibmem[i-2] - fibmem[i - life])
        end
    end
    return fibmem[n]
end

println(dpfibonacci(6, 3))
# >>> 4

println(dpfibonacci(81, 19))
# >>> 37773534761266700
