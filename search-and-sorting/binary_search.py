"""
Binary Search

Input: sorted list and the element you are searching for
Output: the index of the element or -1 if the element is not in the list

Runtime: O(logn)

- start at the middle of the list
- if the element you are looking for is less than the middle element, recursively search the left half
- if the element you are looking for is greater than the middle element, recursively search the right half
- we expect to cut the list in half each time so runtime is O(logn)
"""


def binary_search(lst, x):
    if not lst:
        return -1

    def search(lst, x, lo, hi):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2

        if lst[mid] == x:
            return mid

        if x < lst[mid]:
            return search(lst, x, lo, mid - 1)
        elif x > lst[mid]:
            return search(lst, x, mid + 1, hi)

    return search(lst, x, 0, len(lst) - 1)


assert binary_search([-4, -2, 0, 3, 4, 6, 10], -2) == 1
assert binary_search([], 0) == -1
assert binary_search([-4, -2, 0, 3, 4, 6, 10], 1) == -1
assert binary_search([-4, -2, 0, 3, 4, 6, 10], 11) == -1
assert binary_search([-4, -2, 0, 3, 4, 6, 10], 10) == 6
assert binary_search([-4, -2, 0, 3, 4, 6, 10], -6) == -1
