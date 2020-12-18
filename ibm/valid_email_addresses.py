"""
Input: email address as a string
Output: "True" if email address is valid and "False" otherwise

Email addresses are of the form user@domain.extension

Valid HackerRank emails are of the form user@hackerrank.com. Characters of 'user' are:
- starts w/ 1 to 6 lowercase English letters denoted by character class [a-z]
- lowercase letters are followed by optional underscore i.e. 0 or 1 appearence of an underscore
- optional underscore is followed by 0 to 4 digits denoted by character class [0-9]

Example
Input: "abcdef_1234@hackerrank.com"
Output: True
"""


def is_valid(email_address):
    """
    Runtime: O(N), Space: O(1)
    """
    import re
    if re.match(r'[a-z]{1,6}_?[0-9]{0,4}@hackerrank.com', email_address):
        return True
    return False


assert is_valid('julia@hackerrank.com') is True
assert is_valid('julia_@hackerrank.com') is True
assert is_valid('julia_0@hackerrank.com') is True
assert is_valid('julia0_@hackerrank.com') is False
assert is_valid('julia@gmail.com') is False
assert is_valid('asdfghj@hackerrank.com') is False
assert is_valid('jklkj_123456@hackerrank.com') is False
assert is_valid('julia') is False
assert is_valid('julia__123@hackerrank.com') is False
