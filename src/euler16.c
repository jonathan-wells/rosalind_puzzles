/*
Project Euler - Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Convert a decimal argument to binary format stored in an array.
int *dectobin(int n) {
    int exponent = 0;
    while (pow(2, exponent) <= n) {
        ++exponent;
    }
    int *bin = malloc((exponent + 1)*sizeof(int));
    int i = exponent;
    while (n != 0) {
        bin[i] = n%2;
        n = n/2;
        --i;
    }
    bin[i] = exponent;
    return bin;
}

// (A*A)modx = ((Amodx)*(Amodx))modx
int modexponent(int base, int exponent, int mod) {
    int *bin = dectobin(exponent);
    int i, j = 0, k = 0;
    for (i = bin[0]; i > 0; --i) {
        if (bin[i] == 1) {
            ++j;
        }
    }
    int parts[j];
    j = 0;
    for (i = bin[0]; i > 0; --i) {
        if (bin[i] == 1) {
            parts[j] = pow(2, k);
            ++j;
        }
        ++k;
    }
    for (i = 0; i < j; ++i) {
        printf("%d\n", parts[i]);
    }
    return 0;
}

// int digitsum()

int main(int argc, char *argv[]) {
    if (argc <= 2) {
        printf("Needs at least 2 arguments");
        return 0;
    }
    // modexponent(atoi(argv[1]), atoi(argv[2]), 9);
    int x = pow(2, atoi(argv[2]));
    printf("%d", x);
    return 0;
}
