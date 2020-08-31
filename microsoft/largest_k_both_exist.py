"""
Input: array A of N integers
Output: largest integer K > 0 such that both values K and -K exist in array A, or 0 otherwise

Example
Input: [3, 2, -2, 5, -3]
Output: 3

Input: [1, 2, 3, -4]
0

Ideas
- if we have seen our current element's opposite, then update the max_k
- otherwise, if our current element can possibly beat the current max_k, then add it to our seen set
    - if it can't beat our current max_k, then there's no point in adding it to our set
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
