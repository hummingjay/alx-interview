#!/usr/bin/python3
"""
Function to check if you can unlock all boxes
"""


def canUnlockAll(boxes):
    """
    method to check if all boxes are opened
    if all open Return True
    else return False
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
