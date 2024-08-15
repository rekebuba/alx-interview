#!/usr/bin/python3
"""
A Python script that reads from stdin line by line,
computes metrics according to the specified format,
and handles both regular output every 10 lines,
and a SIGINT (Ctrl+C) signal gracefully.
"""
import sys
import re
from typing import Tuple, List, Any


def validity(patterns: List[str], values: Tuple[str | Any, ...]) -> bool:
    """_summary_

    Args:
        patterns (List[str]): _description_
        values (Tuple[str]): _description_

    Returns:
        bool: _description_
    """
    is_valid = True

    for pattern, value in zip(patterns, values):
        if re.match(pattern, value) is None:
            is_valid = False
            break

    return is_valid


def statistics(status_codes: dict, file_size: int) -> None:
    """Print the accumulated statistics.

    Args:
        status_codes (dict): available status in dictionary
        file_size (int): accumulated file size
    """
    print(f"File size: {file_size}")
    for key, value in status_codes.items():
        if value != 0:
            print(f"{key}: {value}")

pattern = r'^([\.|\d]*) - \[([^]]*)\] "([^"]*)" (\d*) (\d*)$'
valid_ip = r'^(\d*.\d*){3}'
valid_date = r'^\d{4}(-\d{2}){2} (\d|:|\.)*'
valid_request = r'^GET \/projects\/260 HTTP\/1.1'
valid_status = r'^.*'
valid_size = r'^.*'

list_of_patterns = [valid_ip, valid_date,
                    valid_request, valid_status, valid_size]

status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0

try:
    for i, line in enumerate(sys.stdin, start=1):
        match = re.match(pattern, line.strip())

        if match is not None and validity(list_of_patterns, match.groups()):
            code = match.group(4)
            size = match.group(5)

            if code in status_codes:
                status_codes[code] += 1

            file_size += int(size)

            if i % 10 == 0:
                statistics(status_codes, file_size)
except (KeyboardInterrupt, EOFError):
    statistics(status_codes, file_size)
