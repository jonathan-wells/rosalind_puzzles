/*
 * Problem 8 - Largest product in a series.
 *
 * The four adjacent digits in the 1000-digit number (euler8.dat) that have the
 * greatest product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits * in the 1000-digit number that have the greatest product. What is the value
 * of this product?
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    FILE *file;
    file = fopen("/Users/jonwells/Code/puzzle_club/data/euler8.dat", "r");
    int array[1000];
    int i;
    for (i = 0; i < 1000; ++i){
        fscanf(file, "%1d", &array[i]);
    }
    fclose(file);

    int psize = atoi(argv[1]);
    int products[1000 - (psize - 1)];
    for (i = 0; i < 1000 - psize; ++i){
        products[i] = 1;
        for (int j = i; j < i + psize; ++j){
            products[i] *= array[j];
        }
    }

    int currmax = 0;
    for (i = 0; i < 1000 - psize; ++i){
        if (products[i] > currmax){
            currmax = products[i];
        }
    }
    printf("%d", currmax);
    return 0;
}
