"""
Input: array of N positive integers in random order (duplicates are possible)
Output: maximum sum that can be generated with more than one pair of array elements, otherwise -1.

I'm assuming the two pairs have to be made up of distinct elements (but not necessarily distinct values).
As in, element i can only be in one pair.

arr[i] <= 1000001

Ideas
- keep an array of indices called used where used[i] indicates that this element is already being used in a pair
- sort the array from least to greatest
- start with summing the two largest elements (largest sum possible for a pair) and find if there's another pair in the
  rest of the array with that sum (two sum method, runtime O(n))
    - array is always sorted, so in two_sum, I can add a check if the sum of last two elements is less than target to
      return False
    - if there isn't another pair, then sum the last element and the 3rd to last element instead and so on until you
      either find another or you exhaust all options? O(n^2) runtime?
    - keep a set or dictionary of sums you've already tried to avoid recomputing?
"""


def max_sum_pairs(arr):
    """
    Runtime: O(NlogN) + O(N^2) = O(N^2), Space: O(N)?
    """
    def two_sum(nums, t):
        """
        Runtime: O(N), Space: O(N)
        """
        # not necessary
        if len(nums) < 2:
            return False

        # not necessary
        if sum(nums[-2:]) < t:
            return False

        seen = set()
        for num in nums:
            complement = t - num
            if complement in seen:
                return True
            seen.add(num)
        return False

    # not necessary
    if len(arr) < 4:
        return -1

    arr.sort()
    sums = set()
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            curr_sum = arr[j] + arr[i]
            if curr_sum not in sums:
                if two_sum(arr[:j] + arr[j + 1: i], curr_sum):
                    return curr_sum
                sums.add(curr_sum)
    return -1


assert max_sum_pairs([25, 4, 28, 1, 5, 1, 17, 2]) == 30
assert max_sum_pairs([25, 15, 28, 1, 6, 17, 2]) == -1
assert max_sum_pairs([1, 1, 1, 1, 1]) == 2
assert max_sum_pairs([]) == -1
assert max_sum_pairs([2]) == -1
assert max_sum_pairs([2, 1]) == -1
assert max_sum_pairs([2, 1, 3]) == -1
assert max_sum_pairs([2, 1, 3, 4]) == 5
assert max_sum_pairs([19, 17, 8, 5, 12, 13]) == 25
