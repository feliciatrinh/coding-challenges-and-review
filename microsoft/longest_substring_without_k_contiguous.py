"""
Input: string s containing only a and b
Output: longest substring of s such that substring does not contain more than two contiguous occurrences of a and b

Runtime: O(n)

Example
Input: "aabbaaaaabb"
Output: "aabbaa"

Input: "aabbaabbaabbaa"
Output: "aabbaabbaabbaa"

Idea
- iterate through the string
- if you get three contig occurrences of a letter, slide the starting index 1 spot to the left of the current index, so
  now you are back down to 2 contig occurrences of the letter
- keep track of the current letter and how many times it has appeared in a row
"""


def longest_substring_wo_k_contiguous(s, k):
    """
    Expanded the solution to include other values of k.
    Runtime: O(n), Space complexity: O(1)
    """
    if k < 1:
        return ""

    longest_substring = ""
    max_len = 0
    start = 0
    freq = 0
    last_char = ""
    for j, char in enumerate(s):
        if char == last_char and freq == k:
            start = j - (k - 1)
            freq = k
        else:
            if char == last_char:
                freq += 1
            else:
                last_char = char
                freq = 1
            if j - start + 1 > max_len:
                max_len = j - start + 1
                longest_substring = s[start:j + 1]
    return longest_substring


def longest_substring_wo_k_contiguous_alt(s, k):
    """
    Expanded the solution to include other values of k.
    Runtime: O(n), Space complexity: O(1)
    """
    if k < 1:
        return ""

    longest_substring = ""
    max_len = 0
    start = 0
    freq = 1
    last_char = ""
    for j, char in enumerate(s):
        if char == last_char:
            freq += 1
        else:
            last_char = char
            freq = 1

        if freq > k:
            start = j - (k - 1)
            freq = k
        else:
            if j - start + 1 > max_len:
                max_len = j - start + 1
                longest_substring = s[start: j + 1]
    return longest_substring


assert longest_substring_wo_k_contiguous("aabbaaaaabb", 2) == "aabbaa"
assert longest_substring_wo_k_contiguous("aabbaaaaabbaabbaabbaabbab", 2) == "aabbaabbaabbaabbab"
assert longest_substring_wo_k_contiguous("aabbaabbaabbaa", 2) == "aabbaabbaabbaa"
assert longest_substring_wo_k_contiguous("aaabb", 2) == "aabb"
assert longest_substring_wo_k_contiguous("aabbaaaaabbaabbaabbaabbab", 1) == "bab"

assert longest_substring_wo_k_contiguous_alt("aabbaaaaabb", 2) == "aabbaa"
assert longest_substring_wo_k_contiguous_alt("aabbaaaaabbaabbaabbaabbab", 2) == "aabbaabbaabbaabbab"
assert longest_substring_wo_k_contiguous_alt("aabbaabbaabbaa", 2) == "aabbaabbaabbaa"
assert longest_substring_wo_k_contiguous_alt("aaabb", 2) == "aabb"
assert longest_substring_wo_k_contiguous_alt("aabbaaaaabbaabbaabbaabbab", 1) == "bab"
