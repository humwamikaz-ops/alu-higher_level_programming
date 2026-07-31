#!/usr/bin/python3
"""Module that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        tmp = [1]
        for i in range(len(prev) - 1):
            tmp.append(prev[i] + prev[i + 1])
        tmp.append(1)
        triangle.append(tmp)

    return triangle
