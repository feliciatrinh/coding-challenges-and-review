"""
Input: two sorted arrays of length N
Output: a single, sorted array with all items in non-decreasing order

- arrays are sorted, so you can compare an element from array 1 and an element from array 2 and take the smaller
    - if we choose to pop from the original arrays then we keep going until either array or both arrays are empty
"""


def merge_sorted(arr1, arr2):
    """
    Iterative Solution
    Runtime: O(N), Space: O(N)
    """
    result = []
    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    return result + arr1 + arr2


def merge(arr1, arr2):
    """
    Recursive Solution
    Runtime: O(N), Space: O(N)
    """
    if not arr1:
        return arr2
    elif not arr2:
        return arr1
    elif arr1[0] <= arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    return [arr2[0]] + merge(arr1, arr2[1:])


assert merge_sorted([1, 2, 3], [2, 5, 5]) == [1, 2, 2, 3, 5, 5]
assert merge_sorted([0, 2, 4, 6], [1, 3, 5, 7]) == [0, 1, 2, 3, 4, 5, 6, 7]
assert merge_sorted([0, 0, 3, 3], [1, 1, 5, 5]) == [0, 0, 1, 1, 3, 3, 5, 5]

assert merge([1, 2, 3], [2, 5, 5]) == [1, 2, 2, 3, 5, 5]
assert merge([0, 2, 4, 6], [1, 3, 5, 7]) == [0, 1, 2, 3, 4, 5, 6, 7]
assert merge([0, 0, 3, 3], [1, 1, 5, 5]) == [0, 0, 1, 1, 3, 3, 5, 5]
