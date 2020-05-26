"""
Input: string a and string b consisting of lower case letters
Output: minimum number of characters you need to modify to make a and b anagrams, return -1 if impossible

Assume modifications does not include deletions

Runtime: O(n)
Space Complexity: O(n)

Example 1
Input: pot, top
Output: 0

Example 2
Input: pot, put
Output: 1
Explanation: you can modify o in pot or u in put

Example 3:
Input: puts, put
Output: -1
Explanation: they cannot be anagrams of each other
"""


def mods_to_make_anagram(a, b):
    from collections import Counter

    if len(a) != len(b):
        return -1

    counter_a = Counter(a)
    counter_b = Counter(b)

    intersection = counter_a & counter_b
    only_in_a = counter_a - intersection
    only_in_b = counter_b - intersection

    # Divide by 2 because you can modify a character in either string
    return (sum(only_in_a.values()) + sum(only_in_b.values())) // 2


assert mods_to_make_anagram("pot", "put") == 1
assert mods_to_make_anagram("pot", "top") == 0
assert mods_to_make_anagram("puts", "put") == -1
