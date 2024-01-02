#!/usr/bin/python3
""" Module that contains a function that returns a list of lists of integers
representing the Pascal’s triangle of n """


def pascal_triangle(n):
    """ Function that returns a list of lists of integers representing the
    Pascal’s triangle of n """
    if n > 0:
        pascal = [[1 for _ in range(i + 1)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal
    return []
