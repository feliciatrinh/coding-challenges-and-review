"""
Source:
Input: string s
Output: True if string is a palindrome, False otherwise

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


def pali(str): 
    if len(str) == 1: 
        return True
    str = str.lower()
    str = re.sub(r"\s", "", str)
    letters = Counter()
    for char in str: 
        letters[char] += 1
    odd_only = 0
    for char in str: 
        if letters[char] % 2 != 0: 
            odd_only += 1
    # palindromes can have max 1 character that shows up an odd num of times
    if odd_only > 1:
        return False
    return True
