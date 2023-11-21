#!/usr/bin/python3
"""
Method that determines fewest number of coins
needed to meet agiven amount total from a list
"""


def makeChange(coins, total):
    """
    Function that takes a list of coins
    and desired total then finds least for total
    """

    if total <= 0:
        return 0
    # using bitwise operation odd == 1 even == 0
    if all(value % 2 == 0 for value in coins) and total & 1:
        return -1

    coins.sort(reverse=True)

    count = 0
    tsum = total

    while tsum > 0:
        for num in coins:
            if num <= tsum:
                tsum -= num
                count += 1
                break
    return count
