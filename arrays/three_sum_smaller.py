"""
Source: Leetcode
Input: array of n integers nums and a target
Output: number of index triplets i, j, k with 0 <= i < j < k < n that satisfy nums[i] + nums[j] + nums[k] < target

Example
Input: nums = [-2, 0, 1, 3], target = 2
Output: 2
(-2, 0, 1) and (-2, 0, 3)

Ideas
- sort nums in O(NlogN) time first?
- if i solve it like the three sum closest problem where I find the two sum for each nums[i] and keep a delta variable,
  runtime would be O(N^3)
- after sorting
    - if sum(nums[0] + nums[1] + nums[-1]) >= target, then you can discard nums[-1]?
    - if sum(nums[-3:]) < target then all possible groups of three indices (len(nums) choose 3) will satisfy the condition
- solve two sum smaller
    - sliding window
    - keep a left index and a right index
    - when nums[left] + nums[right] < t then every pair you can make that involves the left index satisfies your conditions
    Example: [1, 2, 3, 4], t = 8 where left = 0 initially and right = 3 initially
    1 + 4 < 8 and the pairs (1, 2), (1, 3), (1, 4) work which is equal to right - left
    - then we increment left and continue
    2 + 4 < 8 and pairs (2, 3), (2, 4) work which is right - left again
    - when nums[left] + nums[right] >= t then it's too much and we decrement right
    - this all works because we sorted nums first
"""


def three_sum_smaller(nums, target):
    """
    Runtime: O(NlogN) + O(N^2) = O(N^2), Space: O(N)
    """
    def two_sum_smaller(arr, t):
        """
        Runtime: O(N), Space: O(1)
        """
        left = 0
        right = len(arr) - 1
        count = 0
        while left < right:
            if arr[left] + arr[right] < t:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

    if len(nums) < 3:
        return 0

    nums.sort()
    num_triplets = 0
    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        num_triplets += two_sum_smaller(nums[i + 1:], target - num)
    return num_triplets


assert three_sum_smaller([-2, 0, 1, 3], 2) == 2
assert three_sum_smaller([1, 2, 3, 4, 5], 9) == 4
assert three_sum_smaller([1, 2, 3, 4], 12) == 4
assert three_sum_smaller([5, 4, 2], 1) == 0
assert three_sum_smaller([10, 9], 9) == 0
