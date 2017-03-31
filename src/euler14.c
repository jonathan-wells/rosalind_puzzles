/*
 * Problem 14 - Longest Collatz sequence
 *
 * The following iterative sequence is defined for the set of positive integers:
 *
 * n → n/2 (n is even)
 * n → 3n + 1 (n is odd)
 *
 * Using the rule above and starting with 13, we generate the following
 * sequence:
 *
 * 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 * It can be seen that this sequence (starting at 13 and finishing at 1)
 * contains 10 terms. Although it has not been proved yet (Collatz Problem), it
 * is thought that all starting numbers finish at 1.
 *
 * Which starting number, under one million, produces the longest chain?
 *
 * N.B.: Once the chain starts the terms are allowed to go above one million.
 */

#include <stdio.h>
#include <stdlib.h>

long int collatz(long int n) {
    long int seqlength = 1;
    while (n != 1) {
        if (n%2 == 0) {
            n /= 2;
        } else {
            n = 3*n + 1;
        }
        seqlength += 1;
    }
    return seqlength;
}

void longestcollatz(long int ulimit) {
    long int maxval = 0;
    long int maxind = 0;
    for (long int i = 1; i < ulimit; ++i) {
        long int cz = collatz(i);
        if (cz > maxval) {
            maxval = cz;
            maxind = i;
        }
    }
    printf("maxind: %ld\nmaxval: %ld", maxind, maxval);
}

int main(int argc, char *argv[]) {
    longestcollatz(atoi(argv[1]));
    return 0;
}
