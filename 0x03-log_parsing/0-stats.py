#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import re
from collections import defaultdict


def main():
    """
    Main function to read log entries from standard input,
    compute total file sizes and status code metrics.
    """
    total_size = 0  # Initialize total file size
    status_counts = defaultdict(int)  # Dictionary to count status codes

    # Regex pattern to match the log entry format
    line_pattern = re.compile(
        r'^(?P<ip>[\d\.]+) - \[(?P<date>[^\]]+)\] '
        r'"(?P<method>GET) (?P<path>.+) HTTP/1\.1" '
        r'(?P<status>\d{3}) (?P<size>\d+)$'
    )

    try:
        # Read lines from standard input
        for line_count, line in enumerate(sys.stdin):
            # Remove leading/trailing whitespace
            line = line.strip()
            # Match the line against the regex pattern
            match = line_pattern.match(line)

            # If the line matches the expected format
            if match:
                # Extract file size and status code
                # Convert file size to integer
                file_size = int(match.group('size'))
                # Get the status code
                status_code = match.group('status')

                # Update total file size and status counts
                # Accumulate total file size
                total_size += file_size
                # Increment the count for the status code
                status_counts[status_code] += 1

            # Print metrics every 10 lines
            if (line_count + 1) % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption and print final metrics
        print_metrics(total_size, status_counts)


def print_metrics(total_size, status_counts):
    """
    Print the total file size and the count of each status code.

    Parameters:
    total_size (int): The total file size accumulated.
    status_counts (defaultdict): The dictionary containing
    counts of status codes.
    """
    print(f'Total file size: {total_size}')  # Print the total file size
    # Sort and print status codes in ascending order
    for status_code in sorted(status_counts.keys()):
        # Output each status code and its count
        print(f'{status_code}: {status_counts[status_code]}')


if __name__ == '__main__':
    # Execute the main function when the script is run
    main()
