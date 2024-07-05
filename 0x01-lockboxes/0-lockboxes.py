#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is always unlocked

    queue = [0]  # Start with the first box

    while queue:
        current = queue.pop(0)

        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
