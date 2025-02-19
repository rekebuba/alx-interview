#!/usr/bin/python3
"""Lockboxes"""
"""
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
        - boxes is a list of lists
        - A key with the same number as a box opens that box
        - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
        - The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.

    Args:
        boxes (a list of lists): contain keys to the other boxes

    Returns:
        boolean: True if all boxes can be opened, else return False
    """
    availableKeys = set(boxes[0])
    openedBoxes = set([0])

    while availableKeys:
        newKeys = set()
        for key in availableKeys:
            if key not in openedBoxes and key < len(boxes):
                openedBoxes.add(key)
                newKeys.update(boxes[key])

        availableKeys = newKeys - openedBoxes

    return len(openedBoxes) == len(boxes)
