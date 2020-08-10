"""
Source: Leetcode
Input: array of integers sorted in ascending order
Output: starting and ending position of target value, return [-1, -1] if target not found

Runtime: O(logn)

Example:
Input: [5, 7, 7, 8, 8, 10]
Output: [3, 4]

- elements are in ascending order, so we can use binary search to achieve O(logn) runtime
"""


def first_last_position(nums, target):
    def find_first(target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if target < nums[mid]:
            return find_first(target, start, mid - 1)
        elif target == nums[mid]:
            if mid == 0 or target > nums[mid - 1]:
                return mid
            else:
                return find_first(target, start, mid - 1)
        elif target > nums[mid]:
            return find_first(target, mid + 1, end)

    def find_last(target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if target < nums[mid]:
            return find_last(target, start, mid - 1)
        elif target == nums[mid]:
            if (mid == len(nums) - 1) or target < nums[mid + 1]:
                return mid
            else:
                return find_last(target, mid + 1, end)
        elif target > nums[mid]:
            return find_last(target, mid + 1, end)

    return [find_first(target, 0, len(nums) - 1), find_last(target, 0, len(nums) - 1)]


assert first_last_position([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert first_last_position([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert first_last_position([], 6) == [-1, -1]
