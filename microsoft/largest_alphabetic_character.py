"""
Input: string
Output: Return the uppercase character of the largest alphabetic character whose both lowercase and uppercase appear in
        s, or "NO" otherwise.

Example
Input: "admeDCAB"
Output: "D"

Idea
- keep a set of characters seen
- as you iterate through s
    - if the current char is lowercase, check if the uppercase has already been seen. Same for if char is uppercase
    - update the max_char if req is met

- I can reduce space complexity by only adding a character to the seen set if it's uppercase is > max_char
"""


def largest_alpha_char(s):
    """
    Runtime: O(n), Space complexity: max b/w n and number of unique characters possible, so O(n)?
    """
    seen = set()
    max_char = ''
    for char in s:
        if (char.isupper() and char.lower() in seen) or (char.islower() and char.upper() in seen):
            max_char = max(max_char, char.upper())
        elif char.upper() > max_char:
            seen.add(char)

    if not max_char:
        return 'NO'
    return max_char


assert largest_alpha_char("admeDCAB") == 'D'
assert largest_alpha_char("") == "NO"
assert largest_alpha_char("ABCDEFGHI") == "NO"
assert largest_alpha_char("abcdefghi") == "NO"
