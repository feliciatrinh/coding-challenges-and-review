# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr): 
        if arr[i] == i + 1: 
            i += 1
        else: 
            # swap the element that's out of place w/ the element
            # that's currently at the element's correct position
            # assumes that input array contains consecutive numbers starting from 1
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            swaps += 1
    return swaps
arr = [2, 3, 4, 1, 5]
print(minimumSwaps(arr) == 3)
