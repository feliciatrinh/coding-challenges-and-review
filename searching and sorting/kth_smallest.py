def kth_smallest(arr1, arr2, k):
    """
    Given two sorted array, each of size n, give the kth smallest element
    in the union of the two arrays in log(k) time. 
    Assumes that k > 0 and k <= 2n and that the arrays cannot both be empty. 
    """
    # when an array is empty, return the kth smallest element in the other array
    if len(arr1) == 0:
        return arr2[k - 1]
    elif len(arr2) == 0:
        return arr1[k - 1]
    # base case when k = 1
    if k == 1: 
        return min(arr1[0], arr2[0])
    # compare the median of each array
    i = k // 2
    # if i = length of either array
    # arr[i-1] is the last element of its array
    if i == min(len(arr1), len(arr2)):
        # kth smallest element must be in arr2
        if arr1[i - 1] < arr2[i - 1]:
            return kth_smallest([], arr2, k - i)
        # kth smallest element must be in arr1
        return kth_smallest(arr1, [], k - i)
    if arr1[i] < arr2[i]:
        return kth_smallest(arr1[i+1:], arr2, k - (i + 1))
    return kth_smallest(arr1, arr2[i+1:], k - (i + 1))
