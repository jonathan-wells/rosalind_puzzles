/*
 * Problem 11 - Largest product in a grid
 * In a 20×20 grid, What is the greatest product of four adjacent numbers in
 * the same direction (up, down, left, right, or diagonally)?
 */

#include <stdio>
#include <stdlib>
#include <fstream>

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
    printf("%d", arr[0]);
    return 0;
}
