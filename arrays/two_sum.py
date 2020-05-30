"""
Input: array of integers, target sum
Output: List of indices of the two numbers that sum to the target. 
Assume there is exactly one solution or none. You may not use the same element twice.

Runtime O(n)
"""


def two_sum(nums, target):
    """
    One pass hash table implementation. Check if the complement is in the dictionary
    and return immediately if it is. Otherwise, add the current element to the dictionary.
    Dictionary key, value is number, index.
    """
    ints = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in ints:
            return [ints[complement], i]
        ints[nums[i]] = i


def two_sum_alt(nums, target):
    """
    :return: two integers in nums that sum to target
    """
    have_seen = set()
    for num in nums:
        complement = target - num
        if complement in have_seen:
            return complement, num
        have_seen.add(complement)


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


assert two_sum_alt([-3, 0, 6], 3) == (-3, 6)
assert two_sum_alt([1, 2, 3, 4], 10) is None
