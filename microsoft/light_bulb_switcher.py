"""
Source: Leetcode
Input: array A, contains the order in which the A[k-th] bulb is turned on for bulbs numbered 1 to N
Output: number of moments for which all turned on bulbs are blue

At moment k (for k in range [0, n - 1]), we turn on the A[k] bulb.
A bulb changes color to blue if it is on and all previous bulbs are also turned on.

N integer in range [1, 10^5]
all elements of A are distinct
each element of A is integer in range [1, N]

Example
Input: A = [2, 1, 3, 5, 4]
Output: 3
All turned on bulbs become blue at moments 1, 2 and 4

Input: A = [2, 3, 4, 1, 5]
Output: 2
All turned on bulbs become blue at moments 3, 4

Input: A = [5, 4, 3, 2, 1]
Output: 1
All turned on bulbs become blue at moment 4

Input: [4, 1, 2, 3]
Output: 1
All turned on bulbs become blue at moment 4

Ideas
- when you reach the end of arr, you can always increment moments by 1
- the bulbs turn blue when you fill in the gap
e.g. [3, 2, 1] has a gap in the beginning b/w bulbs that are on until you turn on bulb 1
- keep track of the start and end of the gap?

- sum of positions of all on-bulbs has to equal 1 + 2 + ... + i for index i starting from 1 b/c no bulb beyond i can be
  on for all the on-bulbs to turn blue
- uses the sum formula 1 + 2 + ... + n = n * (n + 1) / 2
- Runtime: O(N), Space: O(N)
"""


def light_bulb(arr):
    """
    Runtime: O(N), Space: O(1)
    """
    on_sum = 0
    moments = 0
    for i, light in enumerate(arr, start=1):
        on_sum += light
        if (i * (i + 1)) // 2 == on_sum:
            moments += 1
    return moments


def light_bulb_alt(arr):
    """
    Runtime: O(N), Space: O(1)
    Keep track of the rightmost bulb that has been turned on.
    Increment moments if the number of bulbs that are on is equal to the rightmost bulb.
    """
    rightmost = 0
    moments = 0
    on_bulbs = 0
    for light in arr:
        rightmost = max(rightmost, light)
        on_bulbs += 1
        if rightmost == on_bulbs:
            moments += 1
    return moments


assert light_bulb([2, 1, 3, 5, 4]) == 3
assert light_bulb([2, 3, 4, 1, 5]) == 2
assert light_bulb([5, 4, 3, 2, 1]) == 1
assert light_bulb([3, 2, 4, 1, 5]) == 2
assert light_bulb([4, 1, 2, 3]) == 1
assert light_bulb([2, 1, 4, 3, 6, 5]) == 3
assert light_bulb([1, 2, 3, 4, 5, 6]) == 6

assert light_bulb_alt([2, 1, 3, 5, 4]) == 3
assert light_bulb_alt([2, 3, 4, 1, 5]) == 2
assert light_bulb_alt([5, 4, 3, 2, 1]) == 1
assert light_bulb_alt([3, 2, 4, 1, 5]) == 2
assert light_bulb_alt([4, 1, 2, 3]) == 1
assert light_bulb_alt([2, 1, 4, 3, 6, 5]) == 3
assert light_bulb_alt([1, 2, 3, 4, 5, 6]) == 6
