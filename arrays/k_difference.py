"""
Input: arr, array of distinct integers and difference k
Output: number of pairs of integers in arr with a difference of k

Runtime: O(n)

Naive
- for each element in arr, see if arr[i] + k is in the arr
- arr[i] in arr takes O(n) time
- Runtime: O(n^2)

Binary Search
- Sorts the array first
- then see if arr[i] + k is in the arr using binary search
- Runtime: O(nlogn)

Best Idea
- add each element of arr into a set
- iterate through arr and check if arr[i] + k is in the set
- Runtime: O(n)
"""


def best_pairs(k, arr):
    if k == 0:
        return 0
    count = 0
    arr_set = set()
    for elem in arr:
        arr_set.add(elem)
    for elem in arr:
        if elem + k in arr_set: 
            count += 1
    return count 


def binary_search(n, arr):
    """
    Returns true if integer n is in sorted array arr using binary search. 
    """
    if len(arr) == 0:
        return False
    median = len(arr) // 2
    if n == arr[median]:
        return True
    elif n < arr[median]:
        return binary_search(n, arr[0:median])
    else:
        return binary_search(n, arr[median + 1:])


def better_pairs(k, arr):
    """
    Sorts the array first O(nlogn) then sees if arr[i] + k is in the arr using binary search.
    """
    count = 0
    arr_sorted = sorted(arr) # note: arr.sorted() return None, sorted() works for any iterable 
    for elem in arr_sorted:
        if binary_search(elem + k, arr_sorted):
            count += 1
    return count


def slow_pairs(k, arr):
    count = 0
    for elem in arr:
        if elem + k in arr:
            count += 1
    return count
