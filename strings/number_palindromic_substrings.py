"""
Source: Leetcode
Input: string
Output: number of palindromic substrings in input

Runtime: O(n^2)
Can have a runtime of O(n) using Manacher's algorithm.

Example
Input: lasagna
Output: 8
Explanation: possible palindromes are asa, l,a,s,a,g,n,a

Input: hellolle
Output: 13
Explanation: possible palindromes are ellolle,lloll,lol,ll,ll,h,e,l,l,o,l,l,e
"""


def count_pali_substr(s):
    """
    :return: the number of palindromic substrings in s using the expand around the center strategy
    Space complexity: O(1)
    """
    def expand(s, left, right):
        """
        Expands from the center and returns the number of palindromic substrings found.
        """
        num_palis = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            num_palis += 1
            left -= 1
            right += 1
        return num_palis

    if len(s) <= 1:
        return len(s)

    count = 0
    for i in range(len(s)):
        # for the center at each letter
        count += expand(s, i, i)
        # for the center b/w two letters
        count += expand(s, i, i + 1)
    return count


def count_pali_substr_alt(s):
    """
    :return: the number of palindromic substrings in s using the dynamic programming strategy
    Subproblem: P(i, j), boolean True if substring between i and j inclusive
                aka s[i:j + 1] is a palindrome
    Base Cases: P(i, i) == True
                P(i, i + 1) = s[i] == s[i + 1]
    Recurrence Relation:
                P(i, j) = ( P(i + 1, j - 1) and (s[i] == s[j]) )
    Space complexity: O(n^2)
    """
    if len(s) <= 1:
        return len(s)

    count = 0
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
                count += 1

    # we start looking for 3 letter substrings: 3-letter substrings' indices
    # differ by 2 so we start at 2
    for diff in range(2, len(s)):
        for i in range(len(s) - diff):
            p[i][i + diff] = p[i + 1][i + diff - 1] and s[i] == s[i + diff]
            if p[i][i + diff]:
                count += 1
    return count


assert count_pali_substr("lasagna") == 8
assert count_pali_substr("hellolle") == 13
assert count_pali_substr_alt("lasagna") == 8
assert count_pali_substr_alt("hellolle") == 13
