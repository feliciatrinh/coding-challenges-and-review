"""
Source: LeetCode
Input: sorted array of size m, sorted array of size n
Output: median of two sorted arrays in time O(log(m + n))

You may assume nums1 and nums2 cannot be both empty.

Runtime: O(log(m + n))

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


def median(nums1, nums2):
    """
    Solution adapted from finding the kth smallest element of the concatenation of two sorted arrays.
    """
    def kth_smallest(nums1, nums2, k):
        """
        :returns the kth smallest element in the concatenation of the two sorted arrays.
        For example, the 0th element would be the 1st smallest (corresponds to k = 1).
        """
        if not nums1:
            return nums2[k - 1]
        elif not nums2:
            return nums1[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        i = min(len(nums1), k // 2)
        j = min(len(nums2), k // 2)
        if nums1[i - 1] < nums2[j - 1]:
            return kth_smallest(nums1[i:], nums2, k - i)
        return kth_smallest(nums1, nums2[j:], k - j)

    total_length = len(nums1) + len(nums2)
    if total_length % 2 == 0:
        return (kth_smallest(nums1, nums2, total_length // 2) + kth_smallest(nums1, nums2, total_length // 2 + 1)) / 2
    return kth_smallest(nums1, nums2, total_length // 2 + 1)


assert median([1, 3], [2]) == 2
assert median([1, 2], [3, 4]) == 2.5
assert median([2, 3, 4, 5, 6], [1]) == 3.5
