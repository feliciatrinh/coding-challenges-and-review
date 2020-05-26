"""
Source: Hackerrank
Input: list of n lists in which each of the n lists is a pair of integers a and b
Output: integer, the total number of occurrences of the greatest integer x in the grid after n steps

Assume n >= 1

Runtime: O(n)

You have an infinite two-dimensional grid, where the bottom left cell is referenced as (1,1) and each cell contains an
initial value of 0. The game consists of n steps; during each step:
- you have two integers a and b.
- increment the value in every (i, j) cell satisfying 1 <= i <= a and 1 <= j <= b by 1.

After performing n such steps, find the maximum value, x, in any cell on the board, and counts the number of
occurrences of x.

Example
Input: ['2 3','3 7', '4 1']
Output: 2

Idea
- output is always going to be at least 1 b/c a and b will each always be at least 1 so some region is always going to
  overlap
- aka (1, 1) will always be one of the cells containing the greatest integer
- you only need to keep track of the current region that contains the max, which will be the region of overlap aka
  the smaller of the current maximum region and the current region in the list
- you don't have to worry about the maximum value itself
"""


def overlapping_region(steps):
    """
    Input: list of lists, each list in steps contains two integers a and b
    """
    max_i, max_j = steps[0]
    for coord in steps[1:]:
        i, j = coord
        max_i = min(max_i, i)
        max_j = min(max_j, j)
    return max_i * max_j


def overlapping_region_str(steps):
    """
    Input: list of n strings in which each string is a pair of integers a and b that are separated by a single space
    """
    max_i, max_j = map(int, steps[0].split(" "))
    for coord in steps[1:]:
        i, j = map(int, coord.split(" "))
        max_i = min(max_i, i)
        max_j = min(max_j, j)
    return max_i * max_j


assert overlapping_region([[2, 3], [3, 7], [4, 1]]) == 2
assert overlapping_region([[40, 50]]) == 2000
assert overlapping_region([[50, 2], [1, 50], [25, 100]]) == 2

assert overlapping_region_str(["2 3", "3 7", "4 1"]) == 2
assert overlapping_region_str(["40 50"]) == 2000
assert overlapping_region_str(["50 2", "1 50", "25 100"]) == 2
