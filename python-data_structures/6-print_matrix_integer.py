#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for i in range(len(row)):
            line += "{:d}".format(row[i])
            if i != len(row) - 1:
                line += " "
        print(line)
