#!/usr/bin/env julia

type Graph
    nodes::Array
    edges::Array{Tuple}
end

function Graph(seq::String)
    nodes = [i for i in 1:length(seq)]
    edges = [(i, j) for i in nodes for j in nodes if i < j]
    return Graph(nodes, edges)
end

function readseq(filename)
    label, seq = [strip(line) for line in open(readlines, filename)]
    @assert count(i->i == 'A', seq) == count(i->i == 'U', seq)
    @assert count(i->i == 'G', seq) == count(i->i == 'C', seq)
    return seq
end

function ncpmatchings(graph::Graph)
    ncp = []
    for i in graph.nodes
        for j in graph.nodes[2i:end]
            println(i, ' ', j)
        end
    end
end

################################################################################
## Catalan Numbers
################################################################################

function rcatalan(n::Int)
    if n <= 1
        return 1
    else
        return sum(rcatalan(k-1)*rcatalan(n-k) for k in 1:n)
    end
end

function catalan(n::Int)
    mem = zeros(Int, n+1, n)
    mem[1, 1] = 1
    mem[2, 1] = 1
    for i in 3:n+1
        for k in 1:n
            mem[i, k] = sum(mem[k-1, 1:end])*sum(mem[n-k, 1:end])
        end
    end
    return mem
end

function main()
    mem = catalan(4)
    print(join(split(string(mem), ';'), '\n'))
end

main()
