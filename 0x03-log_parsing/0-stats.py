#!/usr/bin/python3
"""
Log Parsing Script

This script reads input lines from stdin, computes various metrics,
and prints the results.
"""

import sys
import re


def compute_metrics(lines):
    """
    Computes the total file size and the number of lines by status code.

    Args:
        lines (list): A list of input lines in the specified format.

    Returns:
        tuple: A tuple containing the total file size and a dictionary
        of status code counts.
    """
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    for line in lines:
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET\
                         /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

    return total_size, status_codes


if __name__ == "__main__":
    lines = []
    try:
        while True:
            line = input().strip()
            lines.append(line)
            if len(lines) == 10:
                total_size, status_codes = compute_metrics(lines)
                print("Total file size: {0}".format(total_size))
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print("{0}: {1}".format(code, count))
                lines = []
    except KeyboardInterrupt:
        total_size, status_codes = compute_metrics(lines)
        print("Total file size: {0}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print("{0}: {1}".format(code, count))
