#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for i, num in enumerate(fila):
            print("{:d}".format(num), end='')
            if i < len(fila) - 1:
                print(" ", end='')
        print()
