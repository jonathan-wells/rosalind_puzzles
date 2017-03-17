/*
 * Problem 3 - Largest prime factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isprime(long int n) {
    long int stop = floor(sqrt(n));
    for (long int i = 2; i <= stop; i++){
        if (n%i == 0) {
            return 0;
        }
    }
    return 1;
}

int trialdiv(long int n) {
    long int curr = n;
    long int stop = floor(sqrt(n));
    long int primes [stop];
    long int idx = 0;
    for (long int i = 2; i <= stop; i++) {
        if (curr%i == 0) {
            curr = curr/i;
            primes[idx] = i;
            idx += 1;
        }
    }
    primes[idx] = curr;
    for (long int i = 0; i <= idx; i++) {
        if (isprime(primes[i]) == 1) {
            printf("%ld\n", primes[i]);
        }
    }
    return 0;
}

int main(int argc, char **argv) {
    long int n = atoi(argv[1]);
    // printf("%d", isprime(n));
    printf("Prime factors of %ld are:\n", n);
    trialdiv(n);
    return 0;
}
