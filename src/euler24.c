#include <stdio.h>
// #include <math.h>

unsigned factorial(unsigned n) {
    unsigned fac = 1;
    while (n > 1) {
        fac *= n;
        --n;
    }
    return fac;
}

int main() {
    int iterable[3] = {0, 1, 2};
    unsigned nperms = factorial(3);
    int permutations[3][nperms];
    for (int i = 0; i <)
    printf("%d", nperms);
    return 0;
}
