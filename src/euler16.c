/*
Project Euler - Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {
    int exponent = atoi(argv[1]);
    int ndigits = floor(1 + exponent*log10(2));

    // Initialise array of zeros, last position set to 2**0 = 1.
    int digits[ndigits];
    for (int i = 0; i < ndigits; ++i) {
        digits[i] = 0;
    }
    digits[ndigits - 1] = 1;

    // For each position in array, double value and carry the one if neccesary.
    int doubled, carry;
    for (int i = 0; i < exponent; ++i) {
        for (int j = ndigits - 1; j >= 0; --j) {
            doubled = 2*digits[j] + carry;
            carry = 0;
            if (doubled >= 10) {
                carry = 1;
                doubled %= 10;
            }
            digits[j] = doubled;
        }
    }

    // Print the number and the sum of the digits.
    int digitsum = 0;
    printf("2**%d = ", exponent);
    for (int i = 0; i < ndigits; ++i) {
        printf("%d", digits[i]);
        digitsum += digits[i];
    }
    printf("\nNumber of digits: %d\n", ndigits);
    printf("Sum of digits: %d", digitsum);
}
