"""
Input: nums, array of integers
Output: the maximum difference between elements nums[j] and nums[i] where j > i, or -1 if there is no such difference

Runtime: O(n)

Naive
- compare between every element

Better
- keep track of the minimum element that's before num[j]
"""


def max_difference(nums):
    min_num = nums[0]
    max_diff = -1
    for j in range(1, len(nums) - 1):
        curr_diff = nums[j] - min_num
        if curr_diff > max_diff:
            max_diff = curr_diff
        if nums[j] < min_num:
            min_num = nums[j]
    return max_diff
