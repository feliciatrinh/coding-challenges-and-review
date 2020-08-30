"""
Source: Leetcode
Input: string s, k
Output: longest substring that contains at most k distinct characters

Runtime: O(n)
Space complexity: O(k) where k is the number of unique characters upper bounded by the length of s upper bounded by
the size of the alphabet/charset

Example
Input: "abcbbbbcccbdddadacb", k = 2
Output: "bcbbbbcccb"

Input: "abcddefabc", k = 4
Output: "abcdd"

Brute force:
- find all substrings in O(n^2) time, check each substring for number of distinct characters in O(n)
- overall runtime: O(n^3) where n is the length of s

Better Idea:
- store characters you've already seen and their last seen index in a dictionary
- when the number of unique characters you've seen in this current substring reaches k, slide the start of the window to
  1 index after the last index of the first unique character in this substring
    - i'd need to keep track of the first unique character in each substring somehow or query for it every time we reach
      k unique characters -> would make the runtime O(nk)?
    - remove this character from the dictionary so that the dictionary always has at most 5 keys

- is there a way to keep track of the first unique character of each substring without calculating the min index each
  time to reduce runtime to O(n)
"""


def longest_substring_k_distinct(s: str, k: int) -> str:
    """
    Runtime: O(nk), Space complexity: O(k)
    """
    if k <= 0:
        return ""

    longest_substring = ""
    max_len = 0
    start = 0
    num_unique = 0
    char_to_index = {}
    for j, char in enumerate(s):
        if num_unique == k and char not in char_to_index:
            # remove the 1st unique character seen in this current substring from the dictionary
            min_index = min(char_to_index.values())
            for seen_char in char_to_index:
                if char_to_index[seen_char] == min_index:
                    char_to_index.pop(seen_char)
                    num_unique -= 1
                    break
            # move the start index to the right of the letter whose last appearance comes first
            start = min_index + 1
        else:
            if j - start + 1 > max_len:
                longest_substring = s[start: j + 1]
                max_len = j - start + 1

        if char not in char_to_index:
            num_unique += 1
        char_to_index[char] = j
    return longest_substring


def longest_substring_k_distinct_alt(s: str, k: int) -> str:
    """
    Runtime: O(nk), Space complexity: O(k)
    """
    if k <= 0:
        return ""

    longest_substring = ""
    max_len = 0
    start = 0
    num_unique = 0
    char_to_index = {}
    for j, char in enumerate(s):
        if char not in char_to_index:
            num_unique += 1

        if num_unique > k:
            # remove the 1st unique character seen in this current substring from the dictionary
            min_index = min(char_to_index.values())
            for seen_char in char_to_index:
                if char_to_index[seen_char] == min_index:
                    char_to_index.pop(seen_char)
                    num_unique -= 1
                    break
            # move the start index to the right of the letter whose last appearance comes first
            start = min_index + 1
        else:
            if j - start + 1 > max_len:
                longest_substring = s[start: j + 1]
                max_len = j - start + 1
        char_to_index[char] = j
    return longest_substring


assert longest_substring_k_distinct("abcbbbbcccbdddadacb", 2) == "bcbbbbcccb"
assert longest_substring_k_distinct("abcddefabc", 4) == "abcdd"
assert longest_substring_k_distinct("", 4) == ""

assert longest_substring_k_distinct_alt("abcbbbbcccbdddadacb", 2) == "bcbbbbcccb"
assert longest_substring_k_distinct_alt("abcddefabc", 4) == "abcdd"
assert longest_substring_k_distinct_alt("", 4) == ""
