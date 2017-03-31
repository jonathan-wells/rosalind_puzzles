/*
 * Problem 12 - Highly divisible triangular number
 *
 * The sequence of triangle numbers is generated by adding the natural numbers.
 * So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
 * first ten terms would be:
 *
 * 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
 *
 * Let us list the factors of the first seven triangle numbers:
 *
 *  1: 1
 *  3: 1, 3
 *  6: 1, 2, 3, 6
 * 10: 1, 2, 5, 10
 * 15: 1, 3, 5, 15
 * 21: 1, 3, 7, 21
 * 28: 1, 2, 4, 7, 14, 28
 *
 * We can see that 28 is the first triangle number to have over five divisors.
 * What is the value of the first triangle number to have over five hundred
 * divisors?
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int *primesieve(unsigned int n){
    // Initialise prime sieve with ones.
    if (n >= INT_MAX){
        printf("Integer size limit exceeded");
        exit(1);
    }
    int *primes = malloc((n + 1)*sizeof(int));
    // int primes[n + 1];
    primes[0] = n;
    primes[1] = 0;
    for (int i = 2; i <= n; ++i){
        primes[i] = 1;
    }
    // Shake the sieve.
    for (int i = 2; i <= sqrt(n); ++i){
        for (int j = i*i; j <= n; j += i){
            primes[j] = 0;
        }
    }
    return primes;
}

int *primefactors(unsigned int n){
    if (n >= INT_MAX){
        // Technically I could limit this to sqrt(n), but for practicality...
        printf("Integer size limit exceeded");
        exit(1);
    }
    // Initialise array of prime factors with 0.
    int arrsize = ceil(log2(n));
    int *pfactors = malloc(arrsize*sizeof(int));
    pfactors[0] = arrsize;
    for (int fidx = 1; fidx < arrsize; ++fidx){
        pfactors[fidx] = 0;
    }
    // Use trial division to find prime pfactors
    int fidx = 1;
    int *primes = primesieve(sqrt(n));
    for (int i = 2; i <= primes[0]; ++i){
        if (primes[i] == 1){
            while (n%i == 0){
                pfactors[fidx] = i;
                n /= i;
                fidx += 1;
            }
        }
    }
    free(primes);
    if (n > 1){
        pfactors[fidx] = n;
        fidx += 1;
    }
    pfactors[0] = fidx;
    return pfactors;
}

int numfactors(int n){
    int *pfactors = primefactors(n);
    int pfactorset[pfactors[0] - 1];
    int pfactorcount[pfactors[0] - 1];
    int unique = 0;
    int idx = 0;
    for (int i = 1; i < pfactors[0]; ++i){
        if (pfactors[i] != unique){
            unique = pfactors[i];
            pfactorset[idx] = unique;
            idx += 1;
        }
    }
    // for (int i = 0; i < idx; ++i){
    //     pfactorcount[i] = 0;
    // }
    for (int i = 0; i < idx; ++i){
        pfactorcount[i] = 1;
        for (int j = 1; j < pfactors[0]; ++j){
            if (pfactors[j] == pfactorset[i]){
                pfactorcount[i] += 1;
            }
        }
    }
    free(pfactors);
    int prod = 1;
    for (int i = 0; i < idx; ++i){
        prod *= pfactorcount[i];
    }
    return prod;
}

void triangle_number_divisors(int divs){
    int index = 0;
    int current = 0;
    int nfactors = 0;
    int currmax = 0;
    while (nfactors < divs){
        index += 1;
        current += index;
        nfactors = numfactors(current);
        if (nfactors > currmax){
            currmax = nfactors;
        }
    }
    printf("index\ttrianglenum\tnumfactors\n");
    printf("%d\t%d\t%d\n", index, current, nfactors);
}

int main(int argc, char *argv[]){
    if (argc <= 1){
        printf("needs an argument");
        exit(1);
    }
    triangle_number_divisors(atoi(argv[1]));
    return 0;
}