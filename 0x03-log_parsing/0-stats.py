#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
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
    status_codes = {}

    for line in lines:
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /\
                         projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

    return total_size, status_codes


try:
    lines = []
    while True:
        line = input().strip()
        lines.append(line)
        if len(lines) == 10:
            total_size, status_codes = compute_metrics(lines)
            print(f'Total file size: File size: {total_size}')
            for code in sorted(status_codes):
                print(f'{code}: {status_codes[code]}')
            lines = []
except KeyboardInterrupt:
    total_size, status_codes = compute_metrics(lines)
    print(f'Total file size: File size: {total_size}')
    for code in sorted(status_codes):
        print(f'{code}: {status_codes[code]}')
