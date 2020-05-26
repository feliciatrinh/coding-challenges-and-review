"""
Source: Leetcode
Input: an array containing integers sorted in ascending order rotated about some pivot, integer target
Output: index of the target if found, -1 otherwise

You may assume no duplicate exists in the array.

Runtime: O(logn)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


def search_rotated_arr(nums, target):
    def binary_search(nums, target, lo, hi):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[lo] == target:
            return lo
        elif nums[hi] == target:
            return hi

        # Check if the left half is in ascending order
        if nums[lo] <= nums[mid]:
            if nums[lo] < target < nums[mid]:
                return binary_search(nums, target, lo, mid - 1)
            return binary_search(nums, target, mid + 1, hi)
        else:
            if nums[mid] < target < nums[hi]:
                return binary_search(nums, target, mid + 1, hi)
            return binary_search(nums, target, lo, mid - 1)

    if not nums:
        return -1

    return binary_search(nums, target, 0, len(nums) - 1)


assert search_rotated_arr([4, 5, 6, 7, 0, 1, 2, 3], 0) == 4
assert search_rotated_arr([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated_arr([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
assert search_rotated_arr([5, 1, 2, 3, 4], 1) == 1
