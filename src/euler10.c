/*
 * Problem 10 - Summation of primes
 *
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million.
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Sieve of Eratosthenes
int *primesieve(int n){
    int *primes = malloc(n*4);

    for (int i = 0; i < n; ++i){
        primes[i] = 1;
    }

    for (int i = 2; i < n; ++i){
        for (int j = 2*i; j <= n; j += i){
            primes[j] = 0;
        }
    }

    return primes;
}

int main(int argc, char *argv[]){
    if (argc <= 1){
        exit(1);
    }

    int n = atoi(argv[1]);
    int *p = primesieve(n);
    int sum = 0;

    for (int i = 2; i <= n; ++i){
        if (p[i] == 1){
            sum += i;
        }
    }

    printf("%d", sum);
    return 0;
}
