"""
Input: arrays A and B consisting of N integers each
Output: number of fair indices

An index k is fair if the four sums (A[0] + ... + A[k - 1]), (A[k] + ... + A[N - 1]), (B[0] + ... + B[k - 1]),
(B[k] + ... + B[N - 1]) are all equal.

A and B have to be split into two non-empty arrays each, so k has to be at least 1 and at most len(A) - 2.

N is integer in range [2, 10^5]
each element of A and B is integer in range [-10^9, 10^9]

Example
Input: A = [4, -1, 0, 3], B = [-2, 5, 0, 3]
Output: 2
Fair indices are 2 and 3

Input: A = [2, -2, -3, 3], B = [0, 0, 4, -4]
Output: 1
Fair index is 2

Input: A = [4, -1, 0, 3], B = [-2, 6, 0, 4]
Output: 0

Ideas
- iterate through array A
    - calculate the sum of the subarrays A[:i - 1], A[i:] until the sums are equal
    - if this sum is the same for array B then increment the fair count
    - avoid O(N^2) by adding the ith element to the left sum and subtracting the ith element from the right sum as you
      go along
"""


def fair_indices(A, B):
    """
    Runtime: O(N), Space: O(1)
    """
    leftsum_A = A[0]
    rightsum_A = sum(A[1:])
    leftsum_B = B[0]
    rightsum_B = sum(B[1:])
    count = 0
    for k in range(1, len(A)):
        if leftsum_A == rightsum_A == leftsum_B == rightsum_B:
            count += 1
        leftsum_A += A[k]
        rightsum_A -= A[k]
        leftsum_B += B[k]
        rightsum_B -= B[k]
    return count


def fair_indices_alt(A, B):
    """
    Runtime: O(N), Space: O(1)
    """
    leftsum = 0
    rightsum = sum(A)
    count = 0
    for i in range(len(A) - 1):
        leftsum += A[i]
        rightsum -= A[i]
        if leftsum == rightsum == sum(B[:i + 1]) == sum(B[i + 1:]):
            count += 1
    return count


assert fair_indices([4, -1, 0, 3], [-2, 5, 0, 3]) == 2
assert fair_indices([2, -2, -3, 3], [0, 0, 4, -4]) == 1
assert fair_indices([4, -1, 0, 3], [-2, 6, 0, 4]) == 0
assert fair_indices([3, 2, 6], [4, 1, 6]) == 0
assert fair_indices([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]) == 2

assert fair_indices_alt([4, -1, 0, 3], [-2, 5, 0, 3]) == 2
assert fair_indices_alt([2, -2, -3, 3], [0, 0, 4, -4]) == 1
assert fair_indices_alt([4, -1, 0, 3], [-2, 6, 0, 4]) == 0
assert fair_indices_alt([3, 2, 6], [4, 1, 6]) == 0
assert fair_indices_alt([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]) == 2
