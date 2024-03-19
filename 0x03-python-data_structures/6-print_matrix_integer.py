#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for rows in matrix:
            for colums in rows:
                print("{:d}".format(colums), end=" ")
            print()
    else:
        print()
