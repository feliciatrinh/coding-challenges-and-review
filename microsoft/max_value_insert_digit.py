"""
Input: an integer num
Output: The maximum possible value obtained by inserting one '5' digit inside the decimal representation of num

Assume num is in range [-8000, 8000]

Example
Input: num = 268, digit = 5
Output: 5268

Ideas
- if the number is non-negative
    - iterate through the number from left to right, lets say each digit in number is num[i]
    - insert the digit when num[i] is less than digit
- if the number if negative, you want the absolute value to be as small as possible
    - iterate through the number from left to right
    - insert the digit when num[i] is greater than digit
"""


def insert_digit(num, digit):
    """
    Expanded solution to allow inserting digits besides '5'
    Runtime: O(N), Space: O(1) or O(N)?
    """
    str_num = str(num)
    for i, d in enumerate(str_num):
        if d == '-':
            continue
        d = int(d)
        if (num >= 0 and d < digit) or (num < 0 and d > digit):
            return int(str_num[:i] + str(digit) + str_num[i:])
    return int(str(num) + str(digit))


assert insert_digit(268, 5) == 5268
assert insert_digit(680, 5) == 6850
assert insert_digit(0, 5) == 50
assert insert_digit(-999, 5) == -5999
assert insert_digit(-123, 5) == -1235
assert insert_digit(-123, 0) == -123
assert insert_digit(-624, 6) == -6246
assert insert_digit(9123, 1) == 91231
