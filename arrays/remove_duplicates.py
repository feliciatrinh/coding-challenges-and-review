"""
Source: Leetcode
Input: sorted array of integers
Output: the new length

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
It doesn't matter what you leave beyond the returned length.

Runtime: O(n)
Space complexity: O(1)
"""


def remove_duplicates(nums):
    """
    Solution that leaves behind the duplicates in the rest of the list.
    """
    if len(nums) <= 1:
        return len(nums)

    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return i + 1


def remove_duplicates_alt(nums):
    """
    Solution that actually removes the duplicates from the list.
    """
    length = len(nums)

    i = 1
    while i < length:
        if nums[i - 1] == nums[i]:
            nums.pop(i)
            length -= 1
        else:
            i += 1
    return length


assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

assert remove_duplicates_alt([1, 1, 2]) == 2
assert remove_duplicates_alt([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert remove_duplicates_alt([1]) == 1
assert remove_duplicates_alt([]) == 0


def no_duplicates(lst):
    """
    Solution for old problem statement.
    Given a list (unsorted), returns a (sorted) list with no duplicates.
    Space: O(n)
    """
    no_dup = set()
    for elem in lst:
        no_dup.add(elem)
    return list(no_dup)


def no_duplicates_2(lst):
    """
    Solution for old problem statement.
    Returns a list with no duplicates. Maintains the original order.
    Space: O(n)
    """
    no_dup = set()
    new_lst = []
    for elem in lst:
        if elem not in no_dup:
            no_dup.add(elem)
            new_lst.append(elem)
    return new_lst
