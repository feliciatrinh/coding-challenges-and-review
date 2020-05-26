"""
Source: geeksforgeeks
Input: two sorted arrays (each of size n) and integer k
Output: the kth smallest element in the sorted concatenation of the two sorted arrays

Assume k > 0 and k <= 2n, and both arrays are non-empty.

Runtime: O(logk)

Example 1
Input: arr1=[1, 2, 3, 4], arr2=[5, 6, 7, 8], k= 3
Output: 3

Example 2
Input: arr1=[1, 3, 5, 7], arr2=[2, 4, 6, 8], k= 4
Output: 4

Example 3
Input: arr1=[1, 2, 3, 4], arr2=[5, 6, 7, 8], k= 1
Output: 1

Naive
- Merge both sorted arrays using merge() from merge sort and return the (k - 1)th element

Idea: Divide and Conquer
- we look at the kth/2 smallest element in both arrays
  - if arr1[k // 2] < arr2[k // 2], we know we can discard the first k // 2 elements of arr1 b/c all of these elements should
    be smaller than the first k // 2 elements of arr2 so these elements are actually the smallest k // 2 elements of both
    arrays

You can extend this solution to accommodate 2 input arrays of different sizes or multiple input arrays of the same
length.

TODO: write a solution that returns the kth smallest element in the UNION of arr1 and arr2 by removing duplicate values
      and takes into account input arrays with different sizes.
"""


def kth_smallest(arr1, arr2, k):
    """
    :param arr1: array of length n
    :param arr2: array of length n
    :return: the kth smallest element in the sorted concatenation of the two sorted arrays
    """

    if not arr1:
        return arr2[k - 1]
    elif not arr2:
        return arr1[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    mid = k // 2
    if arr1[mid - 1] < arr2[mid - 1]:
        return kth_smallest(arr1[mid:], arr2, k - mid)
    return kth_smallest(arr1, arr2[mid:], k - mid)


def kth_smallest_different_sizes(arr1, arr2, k):
    """
    Solution that takes into account input arrays with different sizes.
    :param arr1: array of length n
    :param arr2: array of length m
    """
    if not arr1:
        return arr2[k - 1]
    elif not arr2:
        return arr1[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(len(arr1), k // 2)
    j = min(len(arr2), k // 2)
    if arr1[i - 1] < arr2[j - 1]:
        return kth_smallest(arr1[i:], arr2, k - i)
    return kth_smallest(arr1, arr2[j:], k - j)


def kth_smallest_alt(arr1, arr2, k):
    """
    Returns the kth smallest element in the UNION of arr1 and arr2 by removing duplicate values;
    takes into account input arrays with different sizes.
    :param arr1: array of length n
    :param arr2: array of length m
    """
    pass


assert kth_smallest([1, 2, 3, 4], [5, 6, 7, 8], 3) == 3
assert kth_smallest([1, 3, 5, 7], [2, 4, 6, 8], 4) == 4
assert kth_smallest([1, 2, 3, 4], [5, 6, 7, 8], 1) == 1
assert kth_smallest([1, 1, 2, 3], [4, 5, 6, 7], 5) == 4
assert kth_smallest([1, 1, 4, 7], [2, 4, 6, 8], 5) == 4

assert kth_smallest_different_sizes([1, 3, 5, 7, 9, 11], [2, 4, 6, 8], 3) == 3
assert kth_smallest_different_sizes([-3, -1, 2, 3, 5], [-2, 2, 4, 6, 8, 10, 12], 5) == 2
