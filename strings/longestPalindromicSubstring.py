"""
Source: LeetCode
Input: string s
Output: longest palindromic substring in s

Runtime: IS TOO SLOW

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

# consider using a generator instead?

def longestPalindrome(s: str) -> str:
    def isPalindrome(s):
        """ Runtime: O(n) """
        if len(s) < 2:
            return True
        if s[0] != s[-1]:
            return False
        return isPalindrome(s[1:-1])

    def substrings(s):
        """ Runtime: O(n^2) """
        from itertools import combinations
        return [s[i:j] for i, j in combinations(range(len(s) + 1), 2)]

    if isPalindrome(s):
        return s

    # sorted() runtime is O(nlog(n))
    substrs = sorted(substrings(s), key=len, reverse=True)[1:]
    for sub in substrs:
        if isPalindrome(sub):
            return sub
