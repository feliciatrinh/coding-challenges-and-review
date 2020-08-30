"""
Input: array A of N integers
Output: largest integer K > 0 such that both values K and -K exist in array A, or 0 otherwise

Example
Input: [3, 2, -2, 5, -3]
Output: 3

Input: [1, 2, 3, -4]
0
"""


def largest_k(A):
    """
    Runtime: O(n), Space complexity: O(n)
    """
    max_k = 0
    seen = set()
    for k in A:
        if (k < 0 and abs(k) in seen) or (k > 0 and -k in seen):
            max_k = max(max_k, abs(k))
        elif abs(k) > max_k:
            seen.add(k)
    return max_k


assert largest_k([3, 2, -2, 5, -3]) == 3
assert largest_k([1, 2, 3, -4]) == 0
