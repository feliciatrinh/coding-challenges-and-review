"""
Input: an array
Output: mean, median, and mode

- sort it, runtime O(NlogN), space O(N)
"""


def mean_median_mode(arr):
    """
    Runtime: O(NlogN), Space: O(N)
    Without using libraries.
    If there are multiple modes, returns the mode that appears first in the sorted array.
    If you want the mode that appears first in the original array, make a copy of the original and iterate through that
    instead in the last part.
    """
    mean = sum(arr) / len(arr)

    arr.sort()
    mid = len(arr) // 2
    if len(arr) % 2 != 0:
        median = arr[mid]
    else:
        median = (arr[mid - 1] + arr[mid]) / 2

    freq = dict()
    max_freq = 0
    mode = arr[0]
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] > max_freq:
            max_freq = freq[num]
            mode = num
    return mean, median, mode


assert mean_median_mode([1, 3, 4, 2, 6, 5, 8, 7]) == (4.5, 4.5, 1)
assert mean_median_mode([8, -3, 9, -1, 4, 8, 2, -1]) == (3.25, 3.0, -1)
