#!/usr/bin/python3
"""
A Python script that reads from stdin line by line,
computes metrics according to the specified format,
and handles both regular output every 10 lines,
and a SIGINT (Ctrl+C) signal gracefully.
"""
import re


def statistics(status_codes: dict, file_size: int) -> None:
    """Print the accumulated statistics.

    Args:
        status_codes (dict): available status in dictionary
        file_size (int): accumulated file size
    """
    print("File size: {}".format(file_size))
    for key, value in status_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """main"""
    pattern = r'^(\S*) - \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)$'

    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    line_num = 1

    try:
        while True:
            line = input()
            match = re.match(pattern, line)

            if match is not None and len(match.groups()) == 5:
                code = match.group(4)
                size = match.group(5)

                try:
                    file_size += int(size)
                    if code in status_codes:
                        status_codes[code] += 1
                except ValueError:
                    pass

                if line_num % 10 == 0:
                    statistics(status_codes, file_size)

            line_num += 1
    except (KeyboardInterrupt, EOFError):
        statistics(status_codes, file_size)


if __name__ == '__main__':
    main()
