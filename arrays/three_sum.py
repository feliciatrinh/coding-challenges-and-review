"""
Source: leetcode
Input: array nums of n integers
Output: list of all unique triplets that sum to 0 (so a list of lists)

Example 1
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, 0, 1], [-1, -1, 2]]

Idea:
- For each element elem in nums, remove elem from nums. Then, solve the two_sum
  problem with the rest of the list for -1 * elem
- Runtime: O(n^2)

How to prevent duplicate triplets?

- use itertools.groupby(iterable, key=None) but make sure the iterable is sorted
- returns sub-iterators grouped by the value of key(v) so make sure to convert
  the return value into a list if you want to keep it
"""
from itertools import groupby


def three_sum(nums):
    def two_sum(nums, target):
        """
        Given an array of integers, return a list of all pairs that sum to
        target.
        Runtime: O(n) 
        """
        result = []
        have_seen = set()
        for num in nums:
            complement = target - num
            if complement in have_seen:
                # create sorted pairs
                result.append([min(complement, num), max(complement, num)])
            have_seen.add(num)
        return result

    if len(nums) < 3:
        return []

    triplets = []
    have_seen = set()
    for i, num in enumerate(nums):
        # if we've already seen num
        if num in have_seen:
            continue
        have_seen.add(num)
        pairs = two_sum(nums[:i] + nums[i + 1:], -1 * num)
        for pair in pairs:
            a, b = pair
            # create a sorted triplet
            if num <= a:
                triplets.append([num] + pair)
            elif num >= b:
                triplets.append(pair + [num])
            else:
                triplets.append([a, num, b])

    # remove duplicate triplets
    triplets.sort()
    return list(triplets for triplets, _ in groupby(triplets))


def two_sum_alt(nums, target):
    """
    Given an array of integers, return 2 integers in nums that sum to target and None otherwise.
    """
    have_seen = set()
    for num in nums:
        complement = target - num
        if complement in have_seen:
            return complement, num
        have_seen.add(num)


def two_sum_alt_recursive(nums, target, have_seen):
    """
    Given an array of integers, return 2 integers in nums that sum to target and None otherwise.
    """
    if not nums:
        return None

    num = nums[0]
    complement = target - num
    if complement in have_seen:
        return complement, num

    have_seen.add(num)
    return two_sum_alt_recursive(nums[1:], target, have_seen)


def three_sum_alt(nums, target):
    """
    Given an array of integers, return 3 integers in nums that sum to target.
    Runtime: O(n^2)
    """
    for i, num in enumerate(nums):
        two_sum_result = two_sum_alt(nums[:i] + nums[i + 1:], target - num)
        if two_sum_result is not None:
            a, b = two_sum_result
            return num, a, b


def three_sum_alt_recursive(nums, target, index):
    """
    Given an array of integers, return 3 integers in nums that sum to target.
    Runtime: O(n^2)
    """
    if index > len(nums) - 1:
        return None

    two_sum_result = two_sum_alt_recursive(nums[:index] + nums[index + 1:], target - nums[index], set())
    if two_sum_result is None:
        return three_sum_alt_recursive(nums, target, index + 1)
    a, b = two_sum_result
    return nums[index], a, b


assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([-5, 5, 9]) == []
assert three_sum([4, -4]) == []
assert three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
assert three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
                                                                        [-2, -2, 4], [-2, 0, 2]]

assert three_sum_alt([-1, 0, 1, 2, -1, -4], 0) == (-1, 0, 1)
assert three_sum_alt([-5, 5, 9], 0) is None

assert three_sum_alt_recursive([-1, 0, 1, 2, -1, -4], 4, 0) is None
assert three_sum_alt_recursive([8, 1, -2, 5, 6], 12, 0) == (8, -2, 6)
