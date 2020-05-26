"""
Input: list
Output: list with no duplicates

Runtime: O(n)
"""


def no_duplicates(lst):
    """
    Returns a (sorted) list with no duplicates. 
    The list will be sorted because we used a set. 
    Uses additional space for the set
    """
    no_dup = set()
    for elem in lst:
        no_dup.add(elem)
    return list(no_dup)


def no_duplicates_2(lst):
    """
    Returns a list with no duplicates. Maintains the original order.
    Uses additional space for a new list and a set
    """
    no_dup = set()
    new_lst = []
    for elem in lst: 
        if elem not in no_dup: 
            no_dup.add(elem)
            new_lst.append(elem)
    return new_lst
