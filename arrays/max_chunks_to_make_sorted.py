"""
Input: array that is a permutation of [0, 1, ..., arr.length - 1]
Output: max number of chunks we can make for which the sorting algorithm will return a correctly sorted array

array has length in range [1, 10]

Example
Input: [4, 3, 2, 1, 0]
Output: 1

Input: [1, 0, 2, 3, 4]
Output: 4
chunks [1, 0], [2], [3], [4] sorted individually to become [0, 1], [2], [3], [4] then concatenated together in the same
order to become [0, 1, 2, 3, 4]

Ideas
- when the maximum num seen so far equals the index, then you have completed a chunk
"""


def max_chunks(arr):
    """
    Runtime: O(n), Space complexity: O(1)
    """
    max_num = arr[0]
    chunks = 0
    for i in range(len(arr)):
        max_num = max(max_num, arr[i])
        if max_num == i:
            chunks += 1
    return chunks


def max_chunks_hard(arr):
    """
    Elements of array aren't necessarily distinct and input array length can be up to length 2000. Elements could be up
    to 10^8.

    Runtime: O(n), Space: O(n)

    Example
    Input: [5, 4, 3, 2, 1], Output: 1
    Input: [2, 1, 3, 4, 4], Output: 4 chunks are [2, 1], [3], [4], [4]
    """
    # prev_max hold the maximum element of the previous chunks
    prev_max = []
    curr_max = arr[0]
    chunks = 1
    for num in arr[1:]:
        if num >= curr_max:
            chunks += 1
            prev_max.append(curr_max)
            curr_max = num
        else:
            # current chunk should be merged with previous chunks
            while prev_max and num < prev_max[-1]:
                chunks -= 1
                prev_max.pop()
            curr_max = max(curr_max, num)
    return chunks


assert max_chunks([4, 3, 2, 1, 0]) == 1
assert max_chunks([1, 0, 2, 3, 4]) == 4
assert max_chunks([0]) == 1

assert max_chunks_hard([5, 4, 3, 2, 1]) == 1
assert max_chunks_hard([2, 1, 3, 4, 4]) == 4
