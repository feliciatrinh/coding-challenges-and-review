"""
Input: a string representing a sequence of passages delimited by the '|' character
Output: a string representing the passages after filtering for certain rules and duplicates

When comparing for containment, these rules must be followed:
- case of alphabetic characters should be ignored
- leading and trailing whitespace should be ignored
- any other block of contiguous whitespace should be treated as a single space
- non-alphanumerica character should be ignored, white space should be retained

Duplicates must also be filtered.
If two passages are considered equal with respect to the comparison rules listed above, only the shortest should be
retained. If they are the same length, the earlier one in the input sequence should be kept. The retained passages
should be output in their original form (identical to the input passage), and in the same order.

Each test case is a single line comprising the passages (strings) to be processed, delimited by '|' characters. The |
characters are not considered part of any passage.

Ideas
- make passages all lowercase
- get rid of all leading and trailing whitespaces in each passage? .strip()
- convert all blocks of spaces into a single space?
- punctuation counts as non-alphanumeric characters
- if I iterate through the rest of the passages for each passage, runtime is O(M * N^2) where M is the average length
  of a passage and N is the number of passages?
- can us regex pattern matching
- come up with a solution that uses regex and one that doesn't
- can use a trie for faster prefix matching, though you compromise space
"""


def filter_regex(passages):
    """
    Runtime: O(M * N^2) where M is average length of a passage and N is the number of passages
    Space: O(N)
    """
    import re

    passages = passages.split("|")
    passages_copy = passages[:]
    for i in range(len(passages_copy)):
        passage = passages_copy[i].lower().strip(' ')
        # remove any non-alphanumeric characters that aren't spaces
        passage = re.sub(r'[^a-z0-9 ]', '', passage)
        # convert multiple spaces into a single space
        passages_copy[i] = re.sub(r' +', ' ', passage)

    to_remove = set()
    for i in range(len(passages)):
        for j in range(i + 1, len(passages)):
            # duplicate passage
            if passages_copy[i] == passages_copy[j]:
                if len(passages[i]) <= len(passages[j]):
                    to_remove.add(j)
                else:
                    to_remove.add(i)
            # passage[i] is a sub-passage of passage[j]
            elif passages_copy[i] in passages_copy[j]:
                to_remove.add(i)
                # passage[j] is a sub-passage of passage[i]
            elif passages_copy[j] in passages_copy[i]:
                to_remove.add(j)
    return '|'.join([passages[i] for i in range(len(passages)) if i not in to_remove])


def filter_no_regex(passages):
    """
    Runtime: O(M * N^2) where M is average length of a passage and N is the number of passages
    Space: O(N)
    """
    passages = passages.split("|")
    passages_copy = passages[:]
    for i in range(len(passages_copy)):
        # convert to lowercase and convert multiple spaces into a single space, also removes leading and trailing spaces
        passage = ' '.join(passages_copy[i].lower().split())
        new_passage = ''
        for char in passage:
            if char.isalnum() or char == " ":
                new_passage += char

        passages_copy[i] = new_passage

    to_remove = set()
    for i in range(len(passages)):
        for j in range(i + 1, len(passages)):
            # duplicate passage
            if passages_copy[i] == passages_copy[j]:
                if len(passages[i]) <= len(passages[j]):
                    to_remove.add(j)
                else:
                    to_remove.add(i)
            # passage[i] is a sub-passage of passage[j]
            elif passages_copy[i] in passages_copy[j]:
                to_remove.add(i)
            # passage[j] is a sub-passage of passage[i]
            elif passages_copy[j] in passages_copy[i]:
                to_remove.add(j)
    return '|'.join([passages[i] for i in range(len(passages)) if i not in to_remove])


def test(function):
    assert function('IBM cognitive computing|IBM "cognitive" computing is a revolution| ibm cognitive  computing|' +
                    "'IBM Cognitive Computing' is a revolution?") == 'IBM "cognitive" computing is a revolution'
    assert function('"Computer Science Department"|Computer-Science-Department|the "computer science department"')\
           == 'Computer-Science-Department|the "computer science department"'
    assert function('') == ''
    assert function(' | the computer') == ' the computer'
    assert function('apples to oranges|    apples   to    oranges') == 'apples to oranges'
    assert function('apples454|apples4') == 'apples454'
    assert function('1oranges23    |     1oranges23') == '1oranges23    '
    assert function(' duplicate|duplicate| cate ') == 'duplicate'
    assert function(' dup  |duplicate| duplicate ') == 'duplicate'


functions = [filter_regex, filter_no_regex]
for func in functions:
    test(func)
