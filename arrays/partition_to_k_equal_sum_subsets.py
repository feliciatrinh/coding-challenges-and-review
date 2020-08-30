"""
Source: Leetcode
Input: array of integers nums and a positive integer k
Output: True if it's possible to divide this array into k non-empty subsets whose sums are all equal, False otherwise

1 <= k <= len(nums) <= 16
0 < nums[i] < 10^4

Example
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Ideas
- it's not possible if k doesn't divide into sum(nums) evenly, but the converse isn't necessarily true?
- takes O(NlogN) time to sort nums
    - if the largest value is greater than sum(nums) / k then return False?

- backtracking
    - find a subset of nums that sums to sum(nums) / k, keep track of the indices already used, decrement k
    - find another subset that also sums to sum(nums) / k that uses different indices from the first so you need to scan
      through nums again
        - if this element of nums didn't work out then mark it un-used so it can be considered for a different sub-array
"""


def partition(nums, k):
    """
    Runtime: O(k * 2^N)? Space: O(N)
    """
    if k == 1:
        return True

    sum_nums = sum(nums)
    if sum_nums % k != 0:
        return False

    sum_subarray = sum_nums // k
    if max(nums) > sum_subarray:
        return False

    def find_subset(k, curr_sum, start_index):
        """
        :param curr_sum: sum of the current subarray
        :param start_index: next index to check
        """
        if k == 1:
            return True
        # this subarray sums to sum_subarray, so we move onto finding the next one
        if curr_sum == sum_subarray:
            return find_subset(k - 1, 0, 0)

        for i in range(start_index, len(nums)):
            if not used[i] and curr_sum + nums[i] <= sum_subarray:
                used[i] = True
                if find_subset(k, curr_sum + nums[i], i + 1):
                    return True
                else:
                    used[i] = False
        return False

    used = [False for _ in range(len(nums))]
    return find_subset(k, 0, 0)


assert partition([4, 3, 2, 3, 5, 2, 1], 4) is True
assert partition([1, 2, 3, 4, 5], 3) is True
assert partition([1, 1, 5, 3, 8, 6, 2], 5) is False
assert partition([1, 10, 4, 56], 1) is True
assert partition([10, 20, 30], 3) is False
assert partition([2, 2, 2, 2, 3, 4, 5], 4) is False
