"""
Source: leetcode
Input: string s
Output: integer if conversion is successful, 0 otherwise

Runtime: O(n)

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
"""
import re


def my_atoi(str: str) -> int:
    # strip leading whitespace
    str = str.lstrip()
    # the first non-whitespace character in valid strings are -, +, or digits
    # - or + are optional, we look for one or more numerical digits
    match = re.match(r'^[-+]?[0-9]+', str)
    if str == "" or match is None:
        return 0
    return int(match.group())


assert my_atoi("42") == 42
assert my_atoi("   -42") == -42
assert my_atoi("4193 with words") == 4193
assert my_atoi("words and 987") == 0
