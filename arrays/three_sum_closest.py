"""
Source: leetcode
Input: an array nums of n integers and an integer target
Output: sum of three integers in nums that is closest to target

Runtime: O(n^3)???

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
"""


def three_sum_closest(nums, target):
    def two_sum(nums, target):
        """
        Given an array of integers, return True if there are two integers
        that sum to target and False otherwise.
        Runtime: O(n) 
        """
        ints = set()
        for num in nums:
            complement = target - num
            if complement in ints:
                return True
            ints.add(num)
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


assert three_sum_closest([-1, 2, 1, -4], 1) == 2
assert three_sum_closest([-5, -10, -15], 2) == -30
assert three_sum_closest([1,2,4,8,16,32,64,128], 82) == 82
