#!/usr/bin/env julia

type fib_storage
   data::Array{BigInt, 1}

   function fib_storage(data=[1, 1])
       new(data)
   end
end

function push_fib!(storage::fib_storage, val::BigInt)
    push!(storage.data, val)
end

function set_fib(storage::fib_storage, ind::Int, val::BigInt)
    storage.data[ind] = val
end

function get_fib(storage::fib_storage, ind::Int)
    return storage.data[ind]
end

function fib_length(storage::fib_storage)
    return length(storage.data)
end

function dpfibonacci(storage, month::Int)
    if month == 1
        return get_fib(storage, month)
    elseif month == 2
        return get_fib(storage, month)
    elseif fib_length(storage) > month - 2
        pop = get_fib(storage, month - 1) + get_fib(storage, month - 2)
        push_fib!(storage, pop)
        return pop
    else
        pop = dpfibonacci(storage, month-1) + dpfibonacci(storage, month-2)
        push_fib!(storage, pop)
        return pop
    end
end

function main(n::Int, m::Int)
    fibstore = fib_storage()

    for i in 1:n
        pop = dpfibonacci(fibstore, i)
        println(pop)
    end
    pop = dpfibonacci(fibstore, n)
    println(pop)
end

main(10, 3)
