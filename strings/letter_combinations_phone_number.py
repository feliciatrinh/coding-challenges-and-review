"""
Source: leetcode
Input: a string containing digits from 2-9 inclusive
Output: all possible letter combinations that the number could represent

Runtime: exponential?

Iterative solution and recusive solution
"""


def letter_combinations(digits):
    if not digits:
        return []

    letters = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'),
               '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'),
               '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'),
               '9': ('w', 'x', 'y', 'z')}

    prev = [letter for letter in letters[digits[0]]]
    for digit in digits[1:]:
        curr = []
        for substring in prev:
            curr += [substring + letter for letter in letters[digit]]
        prev = curr
    return prev


def letter_combos_recursive(digits):
    """
    Source: leetcode
    Recursive solution
    """
    if not digits:
        return []

    letters = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'),
               '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'),
               '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'),
               '9': ('w', 'x', 'y', 'z')}

    result = []

    def combine(curr, digits):
        if not digits:
            result.append(curr)
        else:
            for letter in letters[digits[0]]:
                combine(curr + letter, digits[1:])

    combine("", digits)
    return result


assert letter_combinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert letter_combinations('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh',
                                      'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg',
                                      'ceh', 'cei', 'cfg', 'cfh', 'cfi']
assert letter_combinations('999') == ["www", "wwx", "wwy", "wwz", "wxw", "wxx", "wxy", "wxz", "wyw", "wyx", "wyy",
                                      "wyz", "wzw", "wzx", "wzy", "wzz", "xww", "xwx", "xwy", "xwz", "xxw", "xxx",
                                      "xxy", "xxz", "xyw", "xyx", "xyy", "xyz", "xzw", "xzx", "xzy", "xzz", "yww",
                                      "ywx", "ywy", "ywz", "yxw", "yxx", "yxy", "yxz", "yyw", "yyx", "yyy", "yyz",
                                      "yzw", "yzx", "yzy", "yzz", "zww", "zwx", "zwy", "zwz", "zxw", "zxx", "zxy",
                                      "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]
assert letter_combinations('2') == ['a', 'b', 'c']

assert letter_combos_recursive('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
