"""
Source: Hackerrank
Input: c, array of binary integers
Output: minimum number of jumps it will take Emma to jump from her starting position to the last cloud.
"""


def jumping_on_clouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1: 
        if i + 2 < len(c) and c[i + 2] == 0: 
            i += 2
        else: 
            i += 1
        jumps += 1
    return jumps
