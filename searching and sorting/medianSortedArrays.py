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


# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
#     sorted_array = []
#     if nums1[-1] <= nums2[0]:
#         sorted_array = nums1 + nums2
#     elif nums2[-1] <= nums1[0]:
#         sorted_array = nums2 + nums2
#     full_length = len(sorted_array)
#     if full_length != 0:
#         if full_length % 2 == 0:
#             return  (sorted_array[full_length // 2]
#                     + sorted_array[full_length // 2 - 1]) / 2
#         return sorted_array[full_length // 2]
        
#     def get_median_indices(length):
#         median_indices = (length // 2, None)
#         if length % 2 == 0:
#             median_indices = (length // 2, length // 2 - 1)
#         return median_indices

#     def mergesort(arr1, arr2):
#         if len(arr1) == 0:
#             return arr2
#         elif len(nums2) == 0:
#             return arr1
#         median_arr1_ind = len(arr1) // 2
#         median_arr2_ind = len(arr2) // 2
#         if arr1[median_arr1_ind] <= arr2[median_arr2_ind]:
#             return arr1[:median_arr1_ind + 1] + mergesort(arr1[])

#     full_len = len(nums1) + len(nums2)
#     left = []
#     right = []
#     while len(nums1) != 0 or len(nums2) != 0:
#         if len(nums1) == 0:
#             sorted_array = left + nums2 + right
#         elif len(nums2) == 0:
#             sorted_array == left + nums1 + right
#         else:
#             median_nums1, _ = get_median_indices(len(nums1))
#             median_nums2, _ = get_median_indices(len(nums2))
