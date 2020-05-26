"""
Merge sort
Input: an unsorted list
Output: a sorted list

Runtime: O(nlogn)
Space complexity: O(n)

Idea:
  - Recursively split list in half, sort each half, merge together
  - Stable sorting
"""


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    return merge(mergesort(lst[:middle]), mergesort(lst[middle:]))


def merge(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif lst1[0] <= lst2[0]:  # use <= for stable sorting
        return [lst1[0]] + merge(lst1[1:], lst2)
    return [lst2[0]] + merge(lst1, lst2[1:])


def inversions(arr):
    """
    Counts the number of inversions using merge sort by including
    a count in the merge step.
    An inversion is formed when two elements are out of order.
    """
