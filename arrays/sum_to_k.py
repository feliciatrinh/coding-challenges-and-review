"""
Input: array of integers (doesn't have to be distinct) and integer k
Output: number of pairs that sum to k

Runtime: O(n)
"""


def sum_to_k(arr, k):
    freq = {}
    for elem in arr:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    count = 0  # counter for number of pairs
    for elem in arr:
        if k - elem in freq:
            # if the pair consists of the same numbers e.g. (1, 1)
            if k - elem == elem:
                # to not count the element and itself as a pair
                count += freq[k - elem] - 1
            else:
                count += freq[k - elem]
    # divide count by 2 because we double-counted when iterating through the list
    # is there a way to avoid double counting?
    return count / 2


arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
arr2 = [1, 1, 1, 1, -1, 3]
assert sum_to_k(arr, 11) == 9
assert sum_to_k(arr2, 2) == 7
