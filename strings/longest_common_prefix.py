"""
Source: Leetcode
Input: list of strings
Output: longest common prefix of all the strings

Runtime: O(s) where s is the total number of characters in all the strings
b/c you have to compare the current longest prefix with every string in strs?

Space complexity: O(1)

All inputs are lower case letters a-z.

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Idea 1
- Scan each string in strs and compare it to the current longest prefix
- The smallest common prefix between the two will become the longest prefix

Idea 2
- Iterate through the characters of the first string in strs
  - while doing this, look at the ith character of each of the other strings in strs
  - b/c you are iterating starting from i = 0, you can return when the length of the current string equals i (aka when
    the current string is the shortest string) or when the two characters don't match (the longest common prefix can't
    be any longer than this)
- Best runtime can be slightly faster as O(kn) where n is the number of strings in strs and k is the length of the shortest
  string, but average runtime is still O(s)
"""


def longest_common_prefix_alt(strs):
    """
    Idea 2, vertical matching
    """
    if not strs:
        return ""

    for i, prefix_char in enumerate(strs[0]):
        for string in strs[1:]:
            # Check the len first just in case it's an empty string
            if len(string) == i or prefix_char != string[i]:
                return strs[0][:i]
    return strs[0]


def longest_common_prefix(strs):
    """
    Idea 1
    """

    def compare(str1, str2):
        if len(str2) > len(str1):
            return compare(str2, str1)

        prefix = ""
        for i, char in enumerate(str2):
            if char == str1[i]:
                prefix += char
            else:
                break
        return prefix

    if not strs:
        return ""

    longest_prefix = strs[0]
    for string in strs[1:]:
        longest_prefix = compare(longest_prefix, string)

    return longest_prefix


assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["abc", "abe"]) == "ab"
assert longest_common_prefix(["", ""]) == ""
assert longest_common_prefix(["a"]) == "a"

assert longest_common_prefix_alt(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix_alt(["dog", "racecar", "car"]) == ""
assert longest_common_prefix_alt(["abc", "abe"]) == "ab"
assert longest_common_prefix_alt(["", ""]) == ""
assert longest_common_prefix_alt(["a"]) == "a"
