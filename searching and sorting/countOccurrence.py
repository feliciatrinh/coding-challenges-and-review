"""
Input: sorted array arr, integer n
Output: number of occurances of n

Runtime: O(logn)

Example 1:
Input: arr=[1, 1, 1], n=5
Output: 0

Example 2:
Input: arr=[1, 2, 2, 3, 4], n = 2
Output: 2

Example 3:
Input: arr=[1, 1, 2, 3, 4], n = 1
Output: 2

Example 4:
Input: arr=[1, 1, 3, 3, 3], n = 3
Output: 3

Example 5:
Input: arr=[1, 1, 1, 1], n = 1
Output: 4

Naive idea:
- iterate through the entire array and count the number of times arr[i] = n
- Runtime: O(n)

Optimal idea:
- use the concept of binary search to locate where the first and last
  occurrence of n is and take advantage of sortedness
- Runtime: O(logn)
"""


def firstOccurrence(arr, n, start, end): 
    """
    Returns the index of the first occurrence of n in arr
    """
    # start at the middle of the arr
    mid = (start + end) // 2

    # occurs when you are looking at only one element
    if start == end:
        if arr[mid] == n:
            return mid
        return None

    # arr[mid] is the first occurrence of n
    if n == arr[mid] and (n > arr[mid - 1] or mid == 0):
        return mid
    # search the left half
    elif n <= arr[mid]:
        return firstOccurrence(arr, n, start, mid - 1)
    # search the right half
    elif n > arr[mid]:
        return firstOccurrence(arr, n, mid + 1, end)


def lastOccurrence(arr, n, start, end): 
    """
    Returns the index of the last occurrence of n in arr
    """
    # start at the middle of the arr
    mid = (start + end) // 2

    # occurs when you are looking at only one element
    if start == end:
        if arr[mid] == n:
            return mid
        return None

    # arr[mid] is the last occurrence of n
    if n == arr[mid] and (n < arr[mid + 1] or n == len(arr) - 1):
        return mid
    # search the left half
    elif n < arr[mid]:
        return lastOccurrence(arr, n, start, mid - 1)
    # search the right half
    elif n >= arr[mid]: 
        return lastOccurrence(arr, n, mid + 1, end)


def countOccurrence(arr, n): 
    """
    Returns the total number of occurrences of n in arr
    """
    end = len(arr) - 1
    first = firstOccurrence(arr, n, 0, end)
    # if n does not appear in arr
    if first is None:
        return 0
    # look in the array after the first occurrence
    last = lastOccurrence(arr, n, first, end)
    return last - first + 1


assert countOccurrence([1, 1, 1], 5) == 0
assert countOccurrence([1, 2, 2, 3, 4], 2) == 2
assert countOccurrence([1, 1, 2, 3, 4], 1) == 2
assert countOccurrence([1, 1, 3, 3, 3], 3) == 3
assert countOccurrence([1, 1, 1, 1], 1) == 4
