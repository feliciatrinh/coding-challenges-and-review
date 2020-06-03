"""
Source: leetcode
Input: a 32-bit signed integer
Output: integer with digits that are the reverse of the input

Runtime: linear in number of digits

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


def reverse_alt(x):
    """
    Space: O(1)
    """
    negative = x < 0
    x = abs(x)
    result = 0
    place = 10**(len(str(x)) - 1)
    while place > 0:
        result += (x % 10) * place
        x //= 10
        place //= 10

    if negative:
        return -1 * result
    return result


def reverse_string(x):
    negative = x < 0
    x = str(abs(x))
    if negative:
        return int("-" + x[::-1])
    return int(x[::-1])


def reverse_string_alt(x):
    x = str(x)
    if x[0] == "-":
        return int("-" + x[1:][::-1])
    return int(x[::-1])


assert reverse(123) == 321
assert reverse_string_alt(-123) == -321
