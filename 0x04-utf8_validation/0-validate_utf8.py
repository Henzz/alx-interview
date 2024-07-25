#!/usr/bin/python3
"""
This module validates utf-8 enconding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    The function takes a list of integers, where each integer
    represents one byte of data. The function returns True if the
    data is a valid UTF-8 encoding, and False otherwise.

    A character in UTF-8 can be 1 to 4 bytes long. The data set can
    contain multiple characters. The data will be represented by a
    list of integers, where each integer represents the 8 least
    significant bits of a byte.

    Args:
        data (list): A list of integers, where each integer represents
        1 byte of data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False
        otherwise.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the binary representation.
        # We only need the least significant 8 bits for any given number,
        # so we discard the rest.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we are to start to count
        # for a new UTF-8 character.
        if n_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            if bin_rep[0] == '0':
                n_bytes = 1
            elif bin_rep[0:3] == '110':
                n_bytes = 2
            elif bin_rep[0:4] == '1110':
                n_bytes = 3
            elif bin_rep[0:5] == '11110':
                n_bytes = 4
            else:
                return False

        # Else, we are to examine the bytes which represent the
        # current UTF-8 character. So, they must adhere to the
        # pattern `10xxxxxx`.
        else:
            if not (bin_rep[0:2] == '10'):
                return False

        # We reduce the number of bytes to process by 1 after each
        # Iteration. This is because we have the complete data for
        # a particular UTF-8 character.
        n_bytes -= 1

    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return n_bytes == 0
