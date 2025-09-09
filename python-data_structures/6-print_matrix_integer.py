#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    i = j = 0
    vertIdx = len(matrix)
    horIdx = len(matrix[i])
    while i < vertIdx:
        j = 0
        while j < horIdx:
            print("{:d}".format(matrix[i][j]),
                  end=" " if j < (horIdx - 1) else "\n")
            j += 1
        i += 1
