#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def validUtf8(self, data: List[int]) -> bool:
    binary = [bin(value)[2:].zfill(8) for value in data]
    valid = True
    length = len(binary)
    i = 0
    while valid and i < length:
        bytes = binary[i].index('0') - 1
        if 4 > bytes > 0:
            i += 1
            while valid and bytes > 0 and i < length:
                valid = binary[i][:2] == '10'
                i += 1
                bytes -= 1
        else:
            valid = binary[i][0] == '0'
            i += 1

    return valid
