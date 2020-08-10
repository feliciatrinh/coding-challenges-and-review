"""
Source: LeetCode
Input: string s
Output: length of the longest substring without repeating characters

Given a string, find the length of the longest substring without repeating characters

Runtime: O(n)
Space complexity: O(k) where k is the number of unique characters upper bounded by the length of s upper bounded by
the size of the alphabet/charset

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Brute force:
- create all possible substrings in O(n^2), check each substring for duplicates in O(n)
- runtime: O(n^3)

Sliding window:
- store current characters i to j - 1 in set
- if char at index j is not in the set, we increment j
- repeat until s[j] is already in the set
- we've found max size of substrings w/o repeats starting at index i
- repeat process for all possible i
    - can optimize by keeping a dictionary of characters mapped to their index in s
    - when s[j] is already in the dictionary, we make the start index of the substrings we're looking at to
      dict[s[j]] + 1. Because we don't need to check every possible i. If we know substring s[i:j] contains a
      duplicate, then we can check the substring s[j + 1: something] on the next iteration which may or may not have any
      duplicates at this point
"""


def longest_substring_unique(s: str) -> str:
    """
    Given a string, return the longest substring without repeating characters. Can adapt to return the length instead.
    Optimal solution, scans the string once with j
    Runtime: O(n), Space complexity: O(k)
    """
    max_len = 0
    start = 0
    longest_substring = ""
    char_to_index = {}
    for j, char in enumerate(s):
        # we need start <= char_to_index[char] for cases like "tmmzuxt" where t repeats at a later index, so our start
        # is no longer <= char_to_index[char]. Otherwise, our answer would be "mzux" instead.
        if char in char_to_index and start <= char_to_index[char]:
            # slide our starting index to the right of the last duplicate
            start = char_to_index[char] + 1
        else:
            if j - start + 1 > max_len:
                longest_substring = s[start:j + 1]
                max_len = j - start + 1
            # max_len = max(max_len, j - start + 1)
        char_to_index[char] = j
    return longest_substring


def longest_substring_sliding(s: str) -> str:
    """
    Runtime: O(n), Space complexity: O(k)
    Worst case, i and j each scan the entire string
    """
    max_len = 0
    longest_substring = ""
    unique_chars = set()
    i = 0
    j = 0
    while i < len(s) and j < len(s):
        if s[j] in unique_chars:
            # remove s[i] from the set of unique chars seen in our current substring
            unique_chars.remove(s[i])
            # slide the window to the right
            i += 1
        else:
            unique_chars.add(s[j])
            if j - i + 1 > max_len:
                max_len = j - i + 1
                longest_substring = s[i:j + 1]
            j += 1
    return longest_substring


def brute_force(s):
    """
    Given a string, return the longest substring without repeating characters.
    Can modify to return the length of the longest substring instead.

    Runtime: O(n^3), Space complexity: O(k) where k is the size of the unique set and upper bounded by n
    """
    def check_unique(string, start, end):
        """
        Returns True if characters in string[start:end] are all unique, False otherwise
        """
        num_unique = set()
        for k in range(start, end):
            if string[k] in num_unique:
                return False
            num_unique.add(string[k])
        return True

    max_len = 0
    longest_substring = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if check_unique(s, i, j):
                if j - i > max_len:
                    longest_substring = s[i:j]
                    max_len = j - i
                # max_len = max(max_len, j - i)
    return longest_substring


def length_of_longest_substring(s: str) -> int:
    """
    First attempt, something like a sliding window approach, not optimal
    """
    # maximum possible length of longest substring is num of unique characters
    max_len = len(set(s))

    # look at windows of s, max_len characters at a time
    # until the number of unique characters in the window
    # equals the number of maximum unique characters of any substring
    while max_len > 1:
        curr_max = 0
        for i in range(len(s)):
            end = i + max_len
            if end <= len(s):
                window = s[i:end]
                window_unique_len = len(set(window))
                if window_unique_len == max_len:
                    return window_unique_len
                if window_unique_len > curr_max:
                    curr_max = window_unique_len
        max_len = curr_max
    return max_len


assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3

assert brute_force("abcabcbb") == "abc"
assert brute_force("bbbbb") == "b"
assert brute_force("pwwkew") == "wke"

assert longest_substring_sliding("abcabcbb") == "abc"
assert longest_substring_sliding("bbbbb") == "b"
assert longest_substring_sliding("pwwkew") == "wke"
assert longest_substring_sliding("tmmzuxt") == "mzuxt"

assert longest_substring_unique("abcabcbb") == "abc"
assert longest_substring_unique("bbbbb") == "b"
assert longest_substring_unique("pwwkew") == "wke"
assert longest_substring_unique("tmmzuxt") == "mzuxt"
