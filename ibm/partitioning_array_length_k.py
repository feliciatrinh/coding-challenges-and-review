"""
Input: array of integers and integer k
Output: "Yes" if it's possible to partition the array into some subsequences of length k each such that
- each element in the array occurs in exactly one subsequence
- all the numbers in a subsequence are distinct
- elements in the array having the same value must be in different subsequences
, or "No" otherwise

Ideas
- backtracking?
- if len(set(subarray)) < k, then this subarray contains duplicates and does not count
- let's say the array can be broken up into m subarrays each of length k
    - if the freq of any number is > m, then return No
- pigeon hole principle
"""


def partition_array(arr, k):
    """
    Runtime: O(N), Space: O(N)
    """
    if not arr or k == 0:
        return "Yes"

    if len(arr) % k != 0:
        return "No"

    m = len(arr) // k
    freq = dict()
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] > m:
            return "No"
    return "Yes"


assert partition_array([1, 2, 3, 4], 2) == "Yes"
assert partition_array([1, 2, 2, 3], 3) == "No"
assert partition_array([1, 1, 1, 1, 1], 1) == "Yes"
assert partition_array([0, 0, 0, 0], 2) == "No"
assert partition_array([2, 1, 2, 1, 2, 1], 2) == "Yes"
