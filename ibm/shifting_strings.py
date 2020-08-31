"""
Input: string s, number of times to shift left, number of times to shift right
Output: string after performing the shifts

Ideas
- convert strings to circular arrays then join the characters together at the end
- the left shifts and right shifts could partially cancel each other out
"""


def shift_strings(s, left_shift, right_shift):
    """
    Runtime: O(N), Space: O(1)
    """
    length = len(s)
    left_shift = left_shift % length
    right_shift = right_shift % length
    if left_shift == right_shift:
        return s

    min_shifts = min(left_shift, right_shift)
    left_shift -= min_shifts
    right_shift -= min_shifts
    if left_shift > 0:
        return s[left_shift:] + s[:left_shift]
    return s[length - right_shift:] + s[:length - right_shift]


assert shift_strings('abcde', 1, 0) == 'bcdea'
assert shift_strings('abcde', 0, 1) == 'eabcd'
assert shift_strings('abcde', 1, 1) == 'abcde'
assert shift_strings('abcde', 7, 2) == 'abcde'
