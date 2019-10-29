# Given an array of distinct integers, count the number of pairs of integers with difference k

# o(n^2) time
def SlowPairs(k, arr):
    """
    For each element in arr, see if arr[i] + k is in the arr
    arr[i] in arr takes O(n) time
    """
    count = 0
    for elem in arr: 
        if elem + k in arr: 
            count += 1
    return count

def binarySearch(n, arr):
    """
    Returns true if integer n is in sorted array arr using binary search. 
    """
    if len(arr) == 0:
        return False
    median = len(arr) // 2
    if n == arr[median]:
        return True
    elif n < arr[median]: 
        return binarySearch(n, arr[0:median])
    else: 
        return binarySearch(n, arr[median + 1:])


def betterPairs(k, arr): 
    """
    Sorts the array first O(nlogn) then sees if arr[i] + k is in the arr by binary search O(logn)
    takes o(nlogn) time overall
    """
    count = 0
    arr_sorted = sorted(arr) # note: arr.sorted() return None, sorted() works for any iterable 
    for elem in arr_sorted: 
        if binarySearch(elem + k, arr_sorted): 
            count += 1
    return count

def bestPairs(k, arr): 
    """
    Puts each element of arr into a set. set.add() takes O(1) on average and O(n) worst case
    so this step takes O(n) on average
    Iterates through arr, checking if arr[i] is in that set in average O(n) time
    checking for existence in the set takes average O(1) and worst case O(n) time
    Worst case scenario would take O(n^2) time
    """
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
