#!/usr/bin/python3
"""Rotate 2D Matrix"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """Dose not return anything, modifies matrix in-place
    by rotating it 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): n x n 2D matrix
    """
    for r in range(len(matrix)):
        for c in range(r, len(matrix[r])):
            # transpose the row and column
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        matrix[r] = matrix[r][::-1]  # reverse the row
