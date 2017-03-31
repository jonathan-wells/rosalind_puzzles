/*
Problem 15 - Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
*/

#include <stdio.h>

unsigned long long int factorial(unsigned long long int n) {
    if ((n <= 1)) {
        return n;
    } else {
        return n * factorial(n-1);
    }
}

unsigned long long int binomcoef(unsigned long long int n, unsigned long long int k) {
    unsigned long long int bc = factorial(n)/(factorial(k)*factorial(n - k));
    return bc;
}

unsigned long long int lattice_paths(unsigned long long int x, unsigned long long int y) {
    int lp = binomcoef(x + y, x);
    return lp;
}

int main() {
    // Good luck! factorials give big numbers very fast...
    unsigned long long int lp = lattice_paths(10, 10);
    printf("%lld", f);
    return 0;
}
