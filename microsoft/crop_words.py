"""
Input: message and character-limit k
Output: new message after cropping a number of words to satisfy the character limit k

Rules
- many not crop away a part of a word
- output may not end with a space
- output message must not exceed k character limit
- output message should be as long as possible

I'm assuming that the original message cannot end in a space either? Even if it meets the character limit.

Ideas
- go backwards through the message and eliminate one character at a time until you've reduced the length of the message
  to k
- possibilities:
    - you keep the entire message as is
    - message ends in a space so you eliminate that space and continue just in case there are multiple spaces in a row
    - you eliminate entire word
        - I need to keep eliminating characters until the last char i saw was a space to not be in the middle of a word
- Runtime: O(n), Space: O(1)
"""


def crop_words(message, k):
    """
    Runtime: O(n), Space: O(1)
    """
    length = len(message)
    if 0 < length <= k and message[-1] != ' ':
        return message

    last_seen = ''
    # i is how many characters you've already removed
    for i in range(length):
        curr_index = length - 1 - i
        if message[curr_index] == ' ':
            last_seen = message[curr_index]
            continue
        if length - i <= k:
            # we've just finished removing an entire word
            if last_seen == ' ':  # if you include 'or i == 0' here, you don't need the special check at the beginning
                return message[:curr_index + 1]
        last_seen = message[curr_index]
    return ''


assert crop_words("Codility We test coders", 14) == "Codility We"
assert crop_words("Codility", 5) == ''
assert crop_words("Codility", 8) == "Codility"
assert crop_words("Codility ", 8) == "Codility"
assert crop_words("Codility ", 10) == "Codility"
assert crop_words("", 1) == ''
assert crop_words(" d ", 3) == ' d'
assert crop_words("   re", 2) == ''
assert crop_words(" co de my", 5) == ' co'
assert crop_words(" co de my", 7) == ' co de'
assert crop_words("  ", 2) == ''
assert crop_words(" c d  ", 5) == ' c d'
assert crop_words("      Codility We test coders     ", 10) == ""
assert crop_words("      Codility We test coders     ", 14) == "      Codility"
