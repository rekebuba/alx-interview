#!/usr/bin/python3
"""Minimum Number of Copy / Paste Operations"""


def minOperations(n) -> int:
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int)

    Returns:
        int: minimum number of operations needed
        to make the resulting string exactly of length n.
    """
    if not isinstance(n, int) or n == 1 or n == 0:
        return 0

    copy = 1
    char = 2
    operations = 2  # initial operation

    while char != n:
        if n % char == 0:
            copy = char  # coping the characters
            operations += 1

        char += copy  # pasting the copied characters
        operations += 1

    return operations
