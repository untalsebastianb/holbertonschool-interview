#!/usr/bin/python3
"""
Rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix,
    rotate it 90 degrees clockwise.
    """
    if not matrix or len(matrix) == 0:
        return
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = tmp
