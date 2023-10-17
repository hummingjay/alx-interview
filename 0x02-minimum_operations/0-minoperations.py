#!/usr/bin/python3
"""
Script that computes to find least number of operations
Uses only two operation Copy all and Paste
"""

def minOperations(n):
    """
    Method that takes in an integer n
    Finds minimum number of operations to get nH characters
    """
    if n < 2:
        return 0
    ans_list = []
    i = 1

    for num in range(2, n + 1):
        i += 1
        if n % i == 0: # check if can copy and paste
            while n % i == 0:
                n /= i
                ans_list.append(i)
    return(sum(ans_list))
