"""
Source: LeetCode
Input: string s
Output: longest palindromic substring in s

Runtime: O(n^2)

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""
def expandAroundCenter(s: str) -> str:
    """
    Source: leetcode
    Runtime: O(n^2), Space complexity: O(1)

    Idea: 
    - palindromes mirror around its center, so palindromes can be expanded
      from its center
    - each string has 2n - 1 possible centers (start from the first letter,
      include the spaces in between letters as possible centers, stop at the
      last letter)

    - Start from a center, look at the letter to the left and the letter to the
      right. If they are the same, then keep expanding outward.

    - Use left and right pointers to keep track of where the center is 
    - left and right pointers begin at index 0. Left and right can either point
      to the same letter, or right can be left + 1
    """
    def expand(s, left, right):
        """
        Expands from the center and returns the length of the palindromic
        substring that is found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # subtract 1 b/c you expanded one extra before the while loop ended
        return right - left - 1

    def isPalindrome(s):
        """ Runtime: O(n) """
        if len(s) < 2:
            return True
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        return False

    # also takes care of when s is the empty string
    if isPalindrome(s):
        return s

    max_left = 0
    max_right = 0
    for i in range(len(s)):
        # for the center at each letter
        letter_len = expand(s, i, i)
        # for the center b/w two letters
        space_len = expand(s, i, i + 1)
        curr_len = max(letter_len, space_len)
        if curr_len > max_right - max_left + 1:
            max_left = i - (curr_len - 1) // 2
            max_right = i + curr_len // 2

    return s[max_left: max_right + 1]


def dynamicLongestPalindrome(s: str) -> str:
    """
    Dynamic programming solution
    Source: leetcode
    Runtime: O(n^2), Space complexity: O(n^2)

    Subproblem: P(i, j), boolean True if substring between i and j inclusive
                aka s[i:j + 1] is a palindrome
    Base Cases: P(i, i) == True
                P(i, i + 1) = s[i] == s[i + 1]
    Recurrence Relation:
                P(i, j) = ( P(i + 1, j - 1) and (s[i] == s[j]) )
    
    - we already look at 2 letter substrings in the second base case, so we
      then look at 3 letter substrings, then 4 letter substrings and so on.
    - if the inside substring is a palindrome, then the entire string is a
      palindrome iff s[i] == s[j]
        - Ex: in "ababa", "bab" is a palindrome so "ababa" is a palindrome b/c
          the first and last letter are the same
    """
    def isPalindrome(s):
        """ Runtime: O(n) """
        if len(s) < 2:
            return True
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        return False

    # also takes care of when s is the empty string
    if isPalindrome(s):
        return s

    longest_pali = s[0]
    # initialize palindrome table
    p = [[False] * len(s) for _ in range(len(s))]
    # base cases
    for i, s_i in enumerate(s):
        for j, s_j in enumerate(s[i:], i):
            if i == j:
                p[i][j] = True
            if j == i + 1:
                p[i][j] = s_i == s_j
            if p[i][j]:
                if j - i + 1 > len(longest_pali):
                    longest_pali = s[i: j + 1]

    # we start looking for 3 letter substrings: 3-letter substrings' indices
    # differ by 2 so we start at 2
    for diff in range(2, len(s)):
        for i in range(len(s) - diff):
            p[i][i + diff] = p[i + 1][i + diff - 1] and s[i] == s[i + diff]
            if p[i][i + diff]:
                # the current palindromic substring has length diff + 1
                if diff + 1 > len(longest_pali):
                    longest_pali = s[i: i + diff + 1]

    return longest_pali


def bruteForceLongestPalindrome(s: str) -> str:
    """
    Brute force solution is to pick all possible starting and ending positions
    for a substring and verify if it's a palindrome.
    Runtime: O(n^3)
    """
    def isPalindrome(s):
        """ Runtime: O(n) """
        if len(s) < 2:
            return True
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        return False

    def substrings(s):
        """ Runtime: O(n^2) """
        from itertools import combinations
        return (s[i:j] for i, j in combinations(range(len(s) + 1), 2))

    if isPalindrome(s):
        return s

    # sorted() runtime is O(nlog(n))
    substrs = sorted(substrings(s), key=len, reverse=True)[1:]
    for sub in substrings(s):
        if isPalindrome(sub):
            return sub

assert expandAroundCenter("aaaa") == "aaaa"
assert expandAroundCenter("babad") == "bab"
assert expandAroundCenter("cbbd") == "bb"
assert expandAroundCenter("abacab") == "bacab"