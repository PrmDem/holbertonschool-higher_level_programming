#!/usr/bin/python3

"""
Divides all elements of a matrix by a given number.

Parameters:
    matrix : list of lists comprised only of int or float types
    div : int or float by which each element of the matrix will be divided.
                Must be a non-zero integer or float.

Returns:
    A new matrix of the same structure as the input, where each element
    is the result of the division of the corresponding element in `matrix`
    by `div`, rounded to 2 decimal places.

Example:
    >>> matrix = [[1, 2], [3, 4]]
    >>> matrix_divided(matrix, 2)
    [[0.5, 1.0], [1.5, 2.0]]
"""


def matrix_divided(matrix, div):
    # Divides all elements in matrix by div
    for row in matrix:
        for item in row:
            if not isinstance(row, list) or not isinstance(item, (int, float)):
                # Ensures matrix is a list of lists of ints/floats
                raise TypeError("matrix must be a matrix (list "
                      "of lists) of integers/floats")

        if len(row) != len(matrix[0]):
            # Ensures all rows from matrix are the same size
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        # Ensures div is a int or float
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
        # Ensures div is not zero

    newMatrix = [[round(nb / div, 2) for nb in row] for row in matrix]
    return newMatrix
    # Return newMatrix composed of divided nb from matrix
