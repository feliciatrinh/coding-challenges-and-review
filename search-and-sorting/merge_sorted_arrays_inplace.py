"""
Source: Leetcode
Input: one array of length m and one array of length n
Output: None

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""


def merge_alt(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    Solution if nums1 didn't have any extra 0s filled in already.
    """
    length = len(nums1)
    i = 0
    while nums2 and i < length:
        element = nums2.pop(0)
        if element < nums1[i]:
            nums1.insert(i, element)
        else:
            nums1.insert(i + 1, element)
            i += 1
        length += 1
        i += 1
    nums1 += nums2


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    nums1 here has 0s filled in, as stated in the original problem.
    nums2 isn't modified at all.

    Start from the back and move forward.
    """
    if not nums2:
        return

    while m > 0 and n > 0:
        # the current element of the final sorted array is the smaller of nums2[n -1] and nums1[m - 1]
        if nums2[n - 1] < nums1[m - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    nums1[:n] = nums2[:n]


nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]
merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 3, 4, 5, 6]

nums1 = [0, 0, 0]
nums2 = [1, 4, 6]
merge(nums1, 0, nums2, 3)
assert nums1 == [1, 4, 6]

nums1 = [1, 4, 6]
nums2 = []
merge(nums1, 3, nums2, 0)
assert nums1 == [1, 4, 6]

nums1 = [1, 3, 0, 0, 0, 0]
nums2 = [0, 2, 4, 6]
merge(nums1, 2, nums2, 4)
assert nums1 == [0, 1, 2, 3, 4, 6]

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 2, 3, 5, 6]
