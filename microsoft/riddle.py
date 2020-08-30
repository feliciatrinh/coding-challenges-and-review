"""
Input: string
Output: a copy of the string with all '?' replaced by lowercase letters (a-z) in such a way that the same letter does
        not occur next to each other.

Multiple outputs possible

Example
Input: "ab?ac?"
Output: "abcaca" or "abzacd" or "abfacf"

Input: "rd?e?wg??"
Output: "rdveawgab"

Idea
- there are 26 lowercase letters a-z
- for each question mark, at most, you have to check the letter before it and the letter after it
    - you can replace the question mark with any letter in a-z that isn't those two letters
    - i can use a random number generator to pick a letter from a set containing letters a-z to get this letter with a
      24/26 probability that it won't be those two letters on the first try
    - Runtime: O(n), Space complexity: O(1) b/c you need a constant amount of space for the 26 letters

    - or you can iterate through your set of a-z and pick the next letter that isn't any of those two letters
    - Runtime and space complexity is the same as above
"""


def no_repeats(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


def riddle(string):
    """
    Runtime: O(n), Space complexity: O(1)
    """
    def get_letter(valid_set, a, b):
        """
        Returns a letter from valid_set that is not a or b.
        """
        for letter in valid_set:
            if letter != a and letter != b:
                return letter

    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'}
    result = ''
    for i in range(len(string)):
        char = string[i]
        if char == "?":
            a = result[i - 1] if i > 0 else ''
            b = string[i + 1] if i < len(string) - 1 else ''
            result += get_letter(alphabet, a, b)
        else:
            result += char
    return result


assert no_repeats("abaacba") is False

assert no_repeats(riddle("ab?ac?")) is True
assert no_repeats(riddle("rd?e?wg??")) is True
assert no_repeats(riddle("??????")) is True
