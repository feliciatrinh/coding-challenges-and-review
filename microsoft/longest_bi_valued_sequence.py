"""
Ideas
- sliding window
- start from the leftmost index
- widen the window until you reach more than 2 distinct elements
- shift the start of the window to the right until you are back down to only 2 distinct elements
    - need to keep track of the last index of each distinct element and the smallest index of these indices?
- runtime: O(N), space: O(N)
"""


def longest_bi_valued_sequence(arr):
    """
    Runtime: O(N), Space: O(N)
    """
    if not arr:
        return 0

    start = 0
    distinct = dict()
    max_len = 0
    for i, num in enumerate(arr):
        distinct[num] = i
        if len(distinct) > 2:
            last_index = len(arr)
            last_elem = 0
            for elem, index in distinct.items():
                if index < last_index:
                    last_index = index
                    last_elem = elem
            distinct.pop(last_elem)

            start = last_index + 1
        else:
            max_len = max(max_len, i - start + 1)
    return max_len


assert longest_bi_valued_sequence([5, 5, 5, 3, 5, 3]) == 6
assert longest_bi_valued_sequence([7, 7, 1, 2, 3, 5, 5, 6, 6]) == 4
assert longest_bi_valued_sequence([1]) == 1
assert longest_bi_valued_sequence([1, 2, 3, 4, 5, 6, 7, 8]) == 2
assert longest_bi_valued_sequence([3, 3, 2, 4, 2, 4, 2, 4, 5, 5]) == 6
