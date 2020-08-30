"""
Input: two arrays, each containing N strings
Output: None

Given two arrays of strings, determine whether corresponding elements contain a common substring.
For each index, print your result on a new line. YES if there is a common substring and NO otherwise.

All strings consist of lowercase English letters only
N is at least 1
each a[i], b[i] has length at least 1

Ideas
- iterate through each array, throw each string into a set, a non-empty intersection shows they two strings share a
  common substring (which could be a single letter)
"""


def two_strings(a, b):
    """
    Runtime: O(N), Space: O(M) where M is longest length of any a[i] or b[i]
    """
    for i in range(len(a)):
        in_a = set(a[i])
        in_b = set(b[i])
        if in_a & in_b:
            print('YES')
        else:
            print('NO')


# should print YES, NO, YES
two_strings(['ab', 'cd', 'ef'], ['af', 'ee', 'ef'])
# should print YES, NO
two_strings(['hello', 'hi'], ['world', 'bye'])
