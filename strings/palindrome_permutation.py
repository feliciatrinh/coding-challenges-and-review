"""
Source:
Input: string s
Output: True if a permutation of string is a palindrome, False otherwise

Example 1:
Input: "a"
Output: True

Example 2:
Input: "racecar"
Output: True

Example 3:
Input: "abd c"
Output: False
"""
import re
from collections import Counter


def palindrome_permutation(string):
    if len(string) == 1:
        return True

    string = re.sub(r"\s", "", string.lower())
    letters = Counter(string)
    odd_only = 0
    for char in string:
        if letters[char] % 2 != 0: 
            odd_only += 1
        # palindromes can have max 1 character that shows up an odd num of times
        if odd_only > 1:
            return False
    return True
