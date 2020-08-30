"""
Source: leetcode
Input: an array nums of n integers and an integer target
Output: sum of three integers in nums that is closest to target

Runtime: O(N^2), Space: O(N)

Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Naive:
- Find all unique triplets possible, calculate the sum of each and return the
  sum closest to target.

Using Three Sum strategy
- For each element elem in nums, remove elem from nums. Then, solve the two_sum
  problem with the rest of the list for (target - elem)
- if the list returned is empty, then iterate through again and solve the
  two_sum problem for (target - elem - delta) and then (target - elem + delta),
  where delta is 1, 2, 3, ... until the solution is found.

Use a sliding window approach
"""


def three_sum_closest(nums, target):
    def two_sum(nums, target):
        """
        Given an array of integers, return True if there are two integers
        that sum to target and False otherwise.
        Runtime: O(n)
        """
        have_seen = set()
        for num in nums:
            complement = target - num
            if complement in have_seen:
                return True
            have_seen.add(num)
        return False

    if len(nums) == 3:
        return sum(nums)

    delta = 0
    while True:
        for i, num in enumerate(nums):
            two_sum_pos = two_sum(nums[:i] + nums[i + 1:], target - num + delta)
            if two_sum_pos:
                return target + delta
            two_sum_neg = two_sum(nums[:i] + nums[i + 1:], target - num - delta)
            if two_sum_neg:
                return target - delta
        delta += 1


def three_sum_closest_alt(nums, target):
    """
    Runtime: O(N^2), Space: O(N)
    """
    if len(nums) == 3:
        return sum(nums)

    nums.sort()
    diff = float('inf')
    for i, num in enumerate(nums):
        if diff == 0 or i > len(nums) - 3:
            break
        left = i + 1
        right = len(nums) - 1
        while left < right:
            three_sum = num + nums[left] + nums[right]
            if abs(target - three_sum) < abs(diff):
                diff = target - three_sum
            if three_sum < target:
                left += 1
            else:
                right -= 1
    # diff = target - three_sum so three_sum = target - diff
    return target - diff


def test(function):
    assert function([-1, 2, 1, -4], 1) == 2
    assert function([-5, -10, -15], 2) == -30
    assert function([1, 2, 4, 8, 16, 32, 64, 128], 82) == 82
    assert function([1, 1, 1, 1], 0) == 3
    assert function([1, 1, 1, 1], -100) == 3


functions = [three_sum_closest, three_sum_closest_alt]
for func in functions:
    test(func)
