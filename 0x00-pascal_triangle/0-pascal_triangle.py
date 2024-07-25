#!/usr/bin/python3
"""
Pascal's Triangle:
    returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if type(n) is not int or n <= 0:
        return [[]]

    triangle = [[1]]
    result = []

    for i in range(n - 1):
        for j in range(len(triangle[i])):
            try:
                result.append(triangle[i][j] + triangle[i][j + 1])
            except IndexError:
                pass

        result.insert(0, 1)
        result.append(1)
        triangle.append(result)
        result = []

    return triangle
