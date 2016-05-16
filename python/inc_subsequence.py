#!/usr/bin/env python

import random

def get_longest_inc_subsequence():
    perm = range(1,100)
    random.shuffle(perm)

    #At each index, i, store the longest sequence length one can get by ending at i and also add the pointer to the previous index in this subseq

    #Need two arrays  backPointer and maxLength
    backPointer = [-1] * len(perm)
    maxLength = [1] * len(perm)
    totMax = 1 #hold the max and store pointer
    totMaxPointer = 1 #hold the max and store pointer
    for i in range(0,len(perm)):
    	j = 0
    	currmax = 0
    	pointer = -1
    	while j < i:
    		if (currmax < maxLength[j]) & (perm[j] < perm[i]):
    			pointer = j
    			currmax = maxLength[j]
    		backPointer[i] = pointer
    		maxLength[i] = currmax + 1
    		j = j+1
    	if maxLength[i] > totMax:
    		totMax = maxLength[i]
    		totMaxPointer = i

    #Now starting from totMaxPointer work through backwards using backPointer to get longest sequence
    longestSeq = [0] * totMax
    newPointer = totMaxPointer #this will be the pointer for the index
    for i in range(1,totMax+1):
    	longestSeq[totMax-i] = perm[newPointer]
    	newPointer = backPointer[newPointer]
    return longestSeq

print(get_longest_inc_subsequence())

def get_longest(n, x):
    pass