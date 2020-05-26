"""
Input: array of non-negative integers
Output: array of indices of those elements that get you to the last index with
        the least number of jumps

Example
Input: [1, 3, 4, 2, 0, 0, 5]
Output: [0, 1, 2, 6], (jumps on elements 1 -> 3 -> 4 -> 5)

Subproblem:
- f(i) is the minimum number of jumps it takes to go from the 0th index to the
  ith index
- Final answer is f(n)

Recurrence relation: 
- f(i) = min {f(i), f(j) + 1} if i <= j + arr[j] for all j < i?

Runtime: O(n^2), there is a linear solution out there though

To get the path, you need to build a prev array and step backwards through that
array at the end.
"""


def least_jumps(arr):
    """
    This solution does not assume that a solution exists but does assume that
    arr cannot be an empty list.
    Runtime: O(n^2)
    Space complexity: O(n)
    """
    f = [len(arr)] * len(arr)
    # Base case
    f[0] = 0
    if len(arr) < 2:
        return f

    prev = [-1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            # check if i is reachable from j
            if i <= j + arr[j]:
                # take the minimum
                if f[j] + 1 < f[i]:
                    f[i] = f[j] + 1
                    prev[i] = j

    last_index = len(arr) - 1
    if prev[last_index] == -1:
        return None

    indices = [last_index]
    while last_index != 0:
        indices.insert(0, prev[last_index])
        last_index = prev[last_index]
    return indices


def canJump(nums):
    """
    Source: leetcode
    Given an array of non-neg integers, you are initially positioned at the
    first index of the array. Each element in the array reps your max jump
    length at that position. Determine if you are able to reach the last index.
    The length of input nums is at least 1.

    Greedy Strategy
    - Iterate from right to left, starting from the last index
    - Mark an index as True if you can reach the leftmost (aka most recent)
      True index from that index. B/c you can hop from True index to True index
      (from left to right) and get to the last index since the last index is
      trivially True
    - Return True if index 0 gets marked True and False otherwise
    - Runtime: O(n)

    Example 1
    Input: [9, 4, 2, 1, 0, 2, 0]
    Bools: [T, T, F, F, F, T, T]

    At each index, you want check if currPos + nums[currPos] >= lastTrueIndex.
    Index 6: trivially True.
    Index 5: 5 + 2 >= 6 so it's True
    Index 4: 4 + 0 < 5 so it's False
    Index 3: 3 + 1 < 5 so it's False
    Index 2: 2 + 2 < 5 so it's False
    Index 1: 1 + 4 >= 5 so it's True
    Index 0: 0 + 9 >= 1 so it's True

    With this strategy, you only need to keep track of the lastTrueIndex.
    Space complexity: O(1)

    """
    lastTrueIndex = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= lastTrueIndex:
            lastTrueIndex = i

    if lastTrueIndex == 0:
        return True
    return False


def jump(nums):
    """
    Source: leetcode
    Input: array of non-neg integers
    Output: minimum number of jumps needed to reach last index from index 0

    Given an array of non-negative integers, you are initially positioned at
    the first index of the array. Each element in the array represents your
    maximum jump length at that position. Your goal is to reach the last index
    in the minimum number of jumps.You can assume that you can always reach the
    last index.
    """
    num_jumps = 0


assert least_jumps([1, 3, 4, 2, 0, 0, 5]) == [0, 1, 2, 6]
assert least_jumps([2, 3, 1, 1, 4]) == [0, 1, 4]
assert least_jumps([1]) == [0]
assert least_jumps([1, 0, 0, 0, 1]) is None
assert canJump([9, 4, 2, 1, 0, 2, 0]) is True
assert canJump([3, 2, 1, 0, 4]) is False
