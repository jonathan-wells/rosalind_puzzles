#!/usr/bin/env julia

###############################################################################
# Disjoint Set
#
# Simple but powerful data structure that contains a set of sets, with some
# unique identifier for each set. There are two methods required to make this
# type useful:
#   find - given an element in a set, return the unique id of that set.
#   union - given two unique sets, delete them and create new merged set.
#
###############################################################################

type DisjointSet
    parents::Dict
    DisjointSet(n::Int) = new(Dict([i => Set([i]) for i in 1:n]))
end

function findparent(djs::DisjointSet, x)
    parent = nothing
    for (parent, set) in djs.parents
        x in set ? break : continue
    end
    return parent
end

function union!(djs::DisjointSet, x, y)
    xp, yp = findparent(djs, x), findparent(djs, y)
    djs.parents[min(xp, yp)] = union(djs.parents[xp], djs.parents[yp])
    pop!(djs.parents, max(xp, yp))
end

###############################################################################
# Graph
#
# Just a container for a set of nodes and edges associated with them. Could add
# lots of useful methods if desired though.
###############################################################################

type Graph
    nodes::Set
    edges::Set
end

function connected_components(G::Graph)
    subgraphs = DisjointSet(max(G.nodes...))
    for (n1, n2) in G.edges
        if findparent(subgraphs, n1) != findparent(subgraphs, n2)
            union!(subgraphs, n1, n2)
        end
    end
    return subgraphs
end

function load_graph(filename)
    data = open(readlines, filename)
    nodes = Set(1:parse(Int, data[1]))
    edges = Set()
    for line in data[2:end]
        edge = tuple([parse(Int, i) for i in split(line)]...)
        push!(edges, edge)
    end
    return Graph(nodes, edges)
end


# Given a file describing a graph, return the number of connected subgraphs.
function main()
    G = load_graph(ARGS[1])
    cc = connected_components(G)
    numcc = length(cc.parents)
    println("Connected components: ", numcc)
    println("Edges needed to build tree: ", numcc - 1)
end

main()
