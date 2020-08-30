"""
Source: Leetcode
Input: array of strings arr
Output: maximum length of a concatenation of a sub-sequence of arr which have unique characters

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters

Ideas
- brute force: form all concatenations possible, see which ones are made up of only unique characters, count those
  characters, keep track of the max
  - only consider a concatenation if they have unique characters
  - we'd end up looking at each string in the array multiple times
  - runtime: O(2^N)? Space: O(2^N)?

- if the string element has a repeat inside it, immediately discard it?
- if the intersection of two strings is not empty, then discard that combo
- otherwise, add the combo to our set
"""


def max_length_concatenated(arr):
    """
    Runtime: O(2^N)? Space: O(2^N)? where N is length of arr
    """
    # start with an empty set so that each string in arr w/o duplicates gets added to concatenations
    concatenations = [set()]
    max_length = 0
    for s in arr:
        # s has duplicate characters
        if len(set(s)) < len(s):
            continue
        s = set(s)
        for con in concatenations:
            # intersection of these two strings is non-empty
            if s & con:
                continue
            concatenations.append(s | con)
            max_length = max(max_length, len(s | con))
    return max_length


assert max_length_concatenated(["un", "iq", "ue"]) == 4
assert max_length_concatenated(["cha", "r", "act", "ers"]) == 6
assert max_length_concatenated(["abcdefghijklmnopqrstuvwxyz"]) == 26
assert max_length_concatenated(["apple", "toast", "bed", "tire", "spon", "cab"]) == 11
