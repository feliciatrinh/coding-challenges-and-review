"""
Input: array of n integers
Output: list of consecutive integers from the array that give the greatest sum

Runtime: O(n)

Example 1:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: [4, -1, 2, 1]

Brute force:
- Calculate the sum of possible subarray and take the maximum
- Runtime: O(n^2)

Kadane's Alg
Subproblem:
- M[i]: the maximum sum of subarrays that end at index i

A[i] is the integer at index i

Recurrence Relation:
- M[i] = max{M[i - 1] + A[i], A[i]}
- Base case: M[0] = A[0]
- maximum sum is max{M[0], M[1], ..., M[n]}


TODO: Divide and Conquer Approach
"""


def maximum_subarray(arr):
    """
    Uses Kadane's algorithm to solve in O(n) time.
    """
    if len(arr) < 2:
        return arr

    M = [0] * len(arr)
    M[0] = arr[0]
    prev = [-1] * len(arr)
    max_sum = arr[0]
    last_index = 0
    for i, A_i in enumerate(arr[1:], 1):
        local_max_sum = max(M[i - 1] + A_i, A_i)
        M[i] = local_max_sum
        if M[i - 1] + A_i > A_i:
            prev[i] = i - 1

        if local_max_sum > max_sum:
            max_sum = local_max_sum
            last_index = i

    # step backwards through prev
    result = []
    while last_index != -1:
        result.insert(0, arr[last_index])
        last_index = prev[last_index]
    return result


assert maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]
assert maximum_subarray([-5]) == [-5]
assert maximum_subarray([-5, 4]) == [4]
assert maximum_subarray([-1, -10]) == [-1]
assert maximum_subarray([]) == []
assert maximum_subarray([0]) == [0]
assert maximum_subarray([-2, 0, -2]) == [0]
