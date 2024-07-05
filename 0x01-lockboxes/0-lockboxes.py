#!/usr/bin/env python3
"""
This module provides a function to determine if all boxes can be unlocked.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes
        and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0].copy()

    while keys:
        key = keys.pop()
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Expected output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Expected output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Expected output: False
