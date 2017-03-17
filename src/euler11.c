/*
 * Problem 11 - Largest product in a grid
 * In a 20×20 grid, What is the greatest product of four adjacent numbers in
 * the same direction (up, down, left, right, or diagonally)?
 */

#include <stdio.h>
#include <stdlib.h>

int *load_array(char filename[50]){
    FILE *file;
    file = fopen(filename, "r");

    int *array;
    array = (int *) malloc(20*20*4);

    for (int i = 0; i < 20; ++i){
        for (int j = 0; j < 20; ++j){
            fscanf(file, "%2d", &array[i*20 +j]);
        }
    }

    fclose(file);
    return array;
}


// BLEURGH

int main(int argc, char *argv[]){
    int *arr = load_array("/Users/jonwells/Code/puzzle_club/data/euler11.dat");

    int psize = atoi(argv[1]);
    int hproducts[20*20 - (psize)];
    int vproducts[20*20 - (psize)];
    int dproducts[20*20 - (psize*psize)];

    int i;
    int j;
    for (i = 0; i < 20*20 - (psize - 1); ++i) hproducts[i] = 1;
    for (i = 0; i < 20*20 - (psize - 1); ++i) vproducts[i] = 1;
    for (i = 0; i < 20*20 - (psize*psize); ++i) dproducts[i] = 1;

    // for (i = 0; i < 20*20 - psize; ++i){
    //     for (int j = i; j < i + psize; ++j){
    //         hproducts[i] *= arr[j];
    //     }
    // }
    // for (i = 0; i < 20*20 - psize; ++i){
    //     for (int j = i; j < i + psize; j = i + 20){
    //         vproducts[i] *= arr[j];
    //     }
    // }
    for (i = 0; i < 20*20 - psize; ++i){
        for (int j = i; j < i + psize; j = i + 21){
            dproducts[i] *= arr[j];
        }
    }

    int currmax = 0;
    // for (i = 0; i < 20*20 - psize; ++i){
    //     if (hproducts[i] > currmax){
    //         currmax = hproducts[i];
    //     }
    // }
    // for (i = 0; i < 20*20 - psize; ++i){
    //     if (vproducts[i] > currmax){
    //         currmax = vproducts[i];
    //     }
    // }
    for (i = 0; i < 20*20 - psize; ++i){
        if (dproducts[i] > currmax){
            currmax = dproducts[i];
        }
    }
    printf("%d", currmax);
    return 0;
}
