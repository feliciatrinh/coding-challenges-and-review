"""
Source: leetcode
Input: a 32-bit signed integer
Output: integer with digits that are the reverse of the input

Runtime: linear in number of digits

Solution is fast, but can I figure out a way to use less memory e.g. a fast
solution w/o the need for a list

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""


def reverse(x: int) -> int:
    negative = x < 0
    x = abs(x)
    digits = []
    while x != 0:
        digits.append(x % 10)
        x = x // 10

    place = 10**(len(digits) - 1)
    result = 0
    while digits:
        result += place * digits.pop(0)
        place //= 10

    if negative:
        return -1 * result
    return result
