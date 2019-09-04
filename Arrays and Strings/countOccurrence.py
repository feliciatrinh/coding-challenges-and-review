# Count the number of occurrences of an integer in a sorted array in big-O logN time
# input args: array arr, integer n to count the occurrences of

# Naive: iterate through the entire array and count the number of times arr[i] = n; linear time
# Optimal: use the concept of binary search to locate where the first and last occurrence of n is
# and take advantage of sortedness; logN time

def firstOccurrence(arr, n): 
    """
    Returns the index of the first occurrence of n in arr
    """
    length = len(arr)
    start = length / 2 # start at the middle of the arr
    if n < arr[start]: # search the left half of the array
        return firstOccurrence(arr[:start - 1], n)
    elif n > arr[start]: # search the right half of the array
        return firstOccurrence(arr[start + 1:], n)
    # arr[start] is the first occurrence or the only element in array is a single n
    elif (n == arr[start] and (n > arr[start - 1] or length == 0)):
        return start
    return -1 # flag to indicate n does not appear in arr

def lastOccurrence(arr, n): 
    """
    Returns the index of the last occurrence of n in arr
    """
    length = len(arr)
    start = length / 2 # start at the middle of the arr
    if n < arr[start]: # search the left half of the array
        return lastOccurrence(arr[:start - 1], n)
    elif n > arr[start]: 
        return lastOccurrence(arr[start + 1:], n)
    # arr[start] is the last occurrence or the only element in array is a single n
    elif (n == arr[start] and (n < arr[start + 1] or length == 0)):
        return start
    return -1 # flag to indicate n does not appear in arr

def countOccurrence(arr, n): 
    """
    Returns the total number of occurrences of n in arr
    """
    first = firstOccurrence(arr, n)
    if first == -1: # if n does not appear in arr
        return 0
    last = lastOccurrence(arr, n)
    return last - first + 1
