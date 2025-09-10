#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareMatx = []
    for row in matrix:
        squRow = list(map(lambda x: x * x, row))
        squareMatx.append(squRow)
    return squareMatx
