#!/usr/bin/python3
"""
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""


def canUnlockAll(boxes):
    """
    This function takes a list of lists and returns a boolean indicating
        whether all boxes in the list can be opened. A key with the same
        number as a box opens that box. You can assume all keys will be
        positive integers. There can be keys that do not have boxes.
        The first box boxes[0] is unlocked.

    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes
        and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key]:
                    stack.append(key)
    return all(visited)
