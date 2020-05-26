"""
Source: LeetCode
Input: string s
Output: length of the longest substring without repeating characters

Given a string, find the length of the longest substring without repeating characters

Runtime: 

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
"""


def length_of_longest_substring(s: str) -> int:
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
