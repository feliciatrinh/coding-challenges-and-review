"""
Source: stackoverflow
Input: string s
Output: True if s is a palindrome, False otherwise

Runtime: O(n)

Example 1:
Input: "racecar"
Output: True

Example 2:
Input: "an a"
Output: False
"""


def is_palindrome(s):
    """ recursive solution """
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False
