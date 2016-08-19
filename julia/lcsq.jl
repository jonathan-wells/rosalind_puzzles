#!/usr/bin/env julia

"""Generate score and pointer matrices

Args:
    s1 - first string
    s2 - second string
Returns:
    matrix - matrix of scores for longest common subseqs
    pointer - record of how scoring matrix was formed, gaps in which seq etc.
"""
function build_matrix(s1::AbstractString, s2::AbstractString)
    matrix = zeros(Int, (length(s1)+1, length(s2)+1))
    pointer = zeros(Int, (length(s1)+1, length(s2)+1))
    m, n = size(matrix)
    for i in 2:m
        for j in 2:n
            # If match, increase score, record diagonal move in pointer
            if s1[i-1] == s2[j-1]
                matrix[i, j] = matrix[i-1, j-1] + 1
                pointer[i, j] = 2
            # If mismatch, maintain score, record move up or across in pointer
            else
                matrix[i, j] = max(matrix[i, j-1], matrix[i-1, j])
                mxval = matrix[i, j]
                mxval == matrix[i, j-1] ? pointer[i, j] = 1 : pointer[i, j] = 3
            end
        end
    end
    return matrix, pointer
end

"Step through scoring matrix (using pointer to guide) and generate lcsq"
function traceback(matrix::Array{Int}, pointer::Array{Int},
                   s1::AbstractString, s2::AbstractString)
    i, j = size(matrix)
    longestsubseq = []
    while matrix[i, j] != 0
        if pointer[i, j] == 2
            i -= 1
            j -= 1
            push!(longestsubseq, s1[i])  # If match, add to longest subseq
        elseif pointer[i, j] == 1
            j -= 1
        elseif pointer[i, j] == 3
            i -= 1
        end
    end
    longestsubseq = join(reverse(longestsubseq))
    return longestsubseq
end

function main(s1, s2)
    # Clean up input strings
    s1 = replace(s1, '\n', "")
    s2 = replace(s2, '\n', "")
    # Generate matrices and print longest common subsequence
    mat, pointer = build_matrix(s1, s2)
    lcsq = traceback(mat, pointer, s1, s2)
    println(lcsq)
    return lcsq
end

s1, s2 = ("ACAGTGCGTTCAAGCAAC", "ACATTTCAATAAGCTA")
main(s1, s2)
