# Count the number of occurrences of an integer in a sorted array in big-O logN time
# input args: array arr, integer n to count the occurrences of

# Naive: iterate through the entire array and count the number of times arr[i] = n; linear time
# Optimal: use the concept of binary search to locate where the first and last occurrence of n is
# and take advantage of sortedness; logN time

"""
TODO: fix this
"""

def firstOccurrence(arr, n, start, end): 
    """
    Returns the index of the first occurrence of n in arr
    """
    mid = (start + end)// 2 # start at the middle of the arr
    # search the right half of the array
    if n > arr[mid]:
        return firstOccurrence(arr, n, mid+1, end)
    # arr[mid] is the first occurrence or the only element in array is a single n
    elif (n == arr[mid] and (n > arr[mid - 1] or mid == 0)):
        return mid
    # search the left half of the array
    elif n <= arr[mid]:
        return firstOccurrence(arr, n, start, mid-1)
    return -1 # flag to indicate n does not appear in arr

def lastOccurrence(arr, n, start, end): 
    """
    Returns the index of the last occurrence of n in arr
    """
    mid = (start + end) // 2 # start at the middle of the arr
    if n < arr[mid]: # search the left half of the array
        return lastOccurrence(arr, n, start, mid-1)
    # arr[mid] is the last occurrence or the only element in array is a single n
    elif (n == arr[mid] and (n < arr[mid + 1] or mid == 0)):
        return mid
    elif n >= arr[mid]: 
        return lastOccurrence(arr, n, mid+1, end)
    return -1 # flag to indicate n does not appear in arr

def countOccurrence(arr, n): 
    """
    Returns the total number of occurrences of n in arr
    """
    end = len(arr) - 1
    first = firstOccurrence(arr, n, 0, end)
    if first == -1: # if n does not appear in arr
        return 0
    # look in the array after the first occurrence
    last = lastOccurrence(arr, n, first, end)
    return last - first + 1
