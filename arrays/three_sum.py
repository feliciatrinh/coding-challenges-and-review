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
        ints = set()
        for num in nums:
            complement = target - num
            if complement in ints:
                # create sorted pairs
                result.append([min(complement, num), max(complement, num)])
            ints.add(num)
        return result

    if len(nums) < 3:
        return []

    triplets = []
    ints = set()
    for i, num in enumerate(nums):
        # if we've already seen num
        if num in ints:
            continue
        ints.add(num)
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


assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([-5, 5, 9]) == []
assert three_sum([4, -4]) == []
assert three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
assert three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
                                                                        [-2, -2, 4], [-2, 0, 2]]
