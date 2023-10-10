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
    # Checks if input is empty
    if not boxes:
        return False

    # get size
    n = len(boxes)
    # set of same length with all false
    visited = [False] * n
    # Initiate stack at first box that's open
    stack = [0]

    # loop through till stack is done
    while stack:
        # set current position (box)
        current_box = stack.pop()
        # set value of visited box to true hence open
        visited[current_box] = True

        # Loop thru box which is a lsit for Keys
        for key in boxes[current_box]:
            # Check validity if 0 < key < n
            # Has not been visited
            if key >= 0 and key < n and not visited[key]:
                # if pass check set key visited
                # set to stack key since now empty
                visited[key]:
                    stack.append(key)
    # all returns true if whole list is true else false
    return all(visited)
