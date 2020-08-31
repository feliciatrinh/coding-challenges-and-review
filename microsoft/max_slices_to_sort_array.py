"""
Input: array A consisting of N distinct integers
Output: max number of slices for which the sorting algorithm will return a correctly sorted array

Sort array A in ascending order using this alg:
Divide array into 1 or more slices (a slice is a contiguous subarray). Sort each slice. Join the sorted slices in the
same order.

N is integer in range [1, 10^5]
each element of A in range [1, 10^9]

Example
Input: [2, 4, 1, 6, 5, 9, 7]
Output: 3
array can be split into 3 slices: [2, 4, 1], [6, 5], [9, 7] that can each be sorted into [1, 2, 4], [5, 6], [7, 9]
then concatenated in the same order into [1, 2, 4, 5, 6, 7, 9]

Input: [4, 3, 2, 1]
Output: 1

Input: [2, 1, 6, 4, 3, 7]
Output: 3
3 slices: [2, 1], [6, 4, 3], [7] sorted into [1, 2], [3, 4, 6], [7]

Ideas
- as I iterate through A
    - I know that if the next num is less than the current num then they have to be in the same slice
    - if the next element is greater than the max element of the current slice, the next element could form a new slice?
    - but if there's a new element that's less than the previous slices' maximum, then you know the new element and
      every other element within the current slice should actually be a part of the prev slice
        - you have to keep checking if the new current slice should be merged with the prev slice
    - keep track of the current slice's max?
    - Runtime: O(N), Space complexity: O(N)
"""


def max_slices(A):
    """
    Runtime: O(N), Space: O(N)
    """
    # prev_max holds the maximum element of the previous slices
    prev_max = []
    curr_max = A[0]
    slices = 1
    for num in A[1:]:
        if num > curr_max:  # if elements weren't distinct, this would be >= instead
            slices += 1
            prev_max.append(curr_max)
        else:
            # current slice should be merged with previous slices
            while prev_max and num < prev_max[-1]:
                slices -= 1
                prev_max.pop()
        curr_max = max(curr_max, num)
    return slices


def max_slices_print(A):
    """
    Runtime: O(N), Space: O(N)
    """
    # prev_max hold the maximum element of the previous slices
    prev_max = []
    curr_max = A[0]
    slices = 1
    s = [[A[0]]]
    for num in A[1:]:
        if num > curr_max:
            slices += 1
            prev_max.append(curr_max)
            s.append([num])
        else:
            # current slice should be merged with previous slices
            while prev_max and num < prev_max[-1]:
                slices -= 1
                prev_max.pop()
                s[slices - 1] += s.pop()
            s[-1].append(num)
        curr_max = max(curr_max, num)
    print(s)
    return slices


assert max_slices([2, 4, 1, 6, 5, 9, 7]) == 3
assert max_slices([4, 3, 2, 1]) == 1
assert max_slices([2, 1, 6, 4, 3, 7]) == 3
assert max_slices([1, 2, 3, 4]) == 4
assert max_slices([1]) == 1
assert max_slices([2, 3, 4, 5, 1]) == 1
assert max_slices([2, 5, 4, 7, 1, 8, 9, 3, 6]) == 1

assert max_slices_print([2, 4, 1, 6, 5, 9, 7]) == 3
assert max_slices_print([4, 3, 2, 1]) == 1
assert max_slices_print([2, 1, 6, 4, 3, 7]) == 3
assert max_slices_print([1, 2, 3, 4]) == 4
assert max_slices_print([1]) == 1
assert max_slices_print([2, 3, 4, 5, 1]) == 1
assert max_slices_print([2, 5, 4, 7, 1, 8, 9, 3, 6]) == 1
