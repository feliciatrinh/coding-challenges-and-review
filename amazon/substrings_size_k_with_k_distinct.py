"""
Input: string s, integer k
Output: list of all unique substrings of s of size k with k distinct characters

Input string only has letters [a-z]
0 <= k <= 26

Ideas
- sliding window
    - if curr character is in your dictionary of seen characters then you have a duplicate
        - slide the start of the window to one index past the index of the last appearance of the duplicate character
        - remember to remove any character that comes before this duplicate character from the dictionary as well
    - if length of current string == k then you have a substring with k distinct characters
    - throw it into a set because this substring isn't necessarily unique among all substrings
    - Runtime: O(N), Space: O(N)? where N is length of string s
"""


def substrings(s, k):
    """
    Runtime: O(N), Space: O(N)
    """
    start = 0
    char_to_index = dict()
    substrings_set = set()
    for i, char in enumerate(s):
        # duplicate character and we slide the start of the window
        if char in char_to_index:
            for j in range(start, char_to_index[char]):
                char_to_index.pop(s[j])
            start = char_to_index[char] + 1
        # our current substring has k distinct characters, slide the start of the window over one
        elif i - start + 1 == k:
            substrings_set.add(s[start: i + 1])
            char_to_index.pop(s[start])
            start += 1
        char_to_index[char] = i

    return list(substrings_set)


def test(result, expected):
    assert len(result) == len(expected)

    for e in expected:
        assert e in result


test(substrings('abcabc', 3), ['abc', 'bca', 'cab'])
test(substrings('abacab', 3), ['bac', 'cab'])
test(substrings('awaglknagawunagwkwagl', 4), ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag",
                                              "nagw", "agwk", "kwag"])
