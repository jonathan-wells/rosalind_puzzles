#!/usr/bin/env julia

function loaddata(filename)
    data = open(readall, filename)
    data = split(data, "\n\n")
    data = [split(i, '\n') for i in data[1:end-1]]
    data = Dict([i[1] => split(i[2], r"\s") for i in data])
    return data
end

function main()
    nwckdata = loaddata("../data/rosalind_nwck.txt")
    for tree in keys(nwckdata)
        s1, s2 = nwckdata[tree][1], nwckdata[tree][2]
        count_brackets(tree, s1, s2)
    end
end

function count_brackets(tree, s1, s2)
    bracketcount = 0
    pattern1 = Regex("$s1(.+)$s2")
    pattern2 = Regex("$s2(.+)$s1")
    if ismatch(pattern1, tree)
        subtree = match(pattern1, tree)
    elseif ismatch(pattern2, tree)
        subtree = match(pattern2, tree)
    end
    subtree = split(subtree[1], "")
    for i in subtree
        if ismatch(r"\(", i)
            bracketcount += 1
        end
    end
    print(bracketcount+2, " ")
end

main()
# count_brackets("Limnaeus_sp", "Homopholis_turtor")
