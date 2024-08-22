#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """method that determines if a given data set represents
    a valid UTF-8 encoding.

    Args:
        data (List[int]): list of integers

    Returns:
        bool: True or False
    """
    valid = all(isinstance(x, int) and x >= 0 and x <= 0x10ffff for x in data)
    binary = [bin(value)[2:].zfill(8) for value in data if valid]
    i = 0
    while valid and i < len(binary):
        try:
            byte = binary[i].index('0') - 1
        except ValueError:
            byte = 0

        if 4 > byte > 0:
            i += 1
            while valid and byte > 0:
                try:
                    valid = binary[i][:2] == '10'
                except IndexError:
                    valid = False
                i += 1
                byte -= 1
        else:
            valid = binary[i][0] == '0'
            i += 1

    return valid
