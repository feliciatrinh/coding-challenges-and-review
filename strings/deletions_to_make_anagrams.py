"""
Source: Hackerrank
Input: string a and string b consisting of lower case letters
Output: minimum number of characters you need to delete to make a and b anagrams

Runtime: O(n)
Space Complexity: O(n)

Can delete characters from either string, the two strings may not be the same length

Idea
- Return the difference between the union and the intersection of the two counters
    - Union are all characters present in either string a and b
    - Intersection is all characters in both string a and b
    - Minimum number of characters we have to delete is the total number of chars that show up in either string but
      aren't in both strings
- Remember that Counter returns 0 when a key is missing
"""


def delete_to_make_anagram(a, b):
    from collections import Counter

    counter_a = Counter(a)
    counter_b = Counter(b)

    intersection = counter_a & counter_b
    union = counter_a | counter_b

    return sum(union.values()) - sum(intersection.values())


assert delete_to_make_anagram("abcd", "abce") == 2
assert delete_to_make_anagram("", "") == 0
assert delete_to_make_anagram("abcdthdfh", "") == 9
assert delete_to_make_anagram("", "kjfls") == 5
assert delete_to_make_anagram("cde", "abc") == 4
assert delete_to_make_anagram("cdehj", "abc") == 6
assert delete_to_make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") == 30
