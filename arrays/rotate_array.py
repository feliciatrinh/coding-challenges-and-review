"""
Source: Leetcode
Input: array of integers
Output: array after rotating it to the right by k steps

k >= 0

Runtime: O(n)
Space: O(1)
"""


def rotate(nums, k):
    k = k % len(nums)
    if k <= 0 or len(nums) <= 1:
        return

    nums[:-k], nums[-k:] = nums[-k:], nums[:-k]


def rotate_alt(nums, k):
    k = k % len(nums)
    while k > 0:
        nums.insert(0, nums.pop())
        k -= 1


def rotate_alt_2(nums, k):
    k = k % len(nums)
    for _ in range(k):
        nums.insert(0, nums.pop())


def rotate_alt_3(nums, k):
    nums[:] = nums[-k:] + nums[:-k]


def rotate_alt_recursive(nums, k):
    k = k % len(nums)
    if k <= 0:
        return
    nums.insert(0, nums.pop())
    rotate_alt_recursive(nums, k - 1)


nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate(nums1, 3)
assert nums1 == [5, 6, 7, 1, 2, 3, 4]

rotate_alt(nums1, 2)
assert nums1 == [3, 4, 5, 6, 7, 1, 2]
