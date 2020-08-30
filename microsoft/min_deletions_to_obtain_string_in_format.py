"""
Input: string s of length N consisting only of letters 'A' and/or 'B'
Output: minimum number of deletions needed to change s to a string such that all A's appear before all B's

Example
Input: "BAAABAB"
Output: 2
Delete the first B and last A to get "AAABB"

Input: "BBABAA"
Output: 3
Delete all A's or delete all B's

Input: "AABBBB"
Output: 0

Ideas
- brute force: explore all ways to delete characters and return the minimum of the combos that resulted in correctly
  formatted strings
  - can keep a set of valid combos you've already seen so you don't repeat?
  - Runtime: O(N * 2^N)? Space: O(N)?

- you can always delete all the A's or delete all the B's to get string in the correct format
    - then min deletions up til now would be min(number of A's, number of B's)
- count how many A's come after the first B and how many B's come before the last A, take minimum as answer?
- this assumes you delete only A's or only B's which is probably not optimal?
"""


def min_deletions_naive(s):
    """
    Brute force method
    Runtime: O(N * 2^N)?, Space: O(N)?
    """
    def is_valid(res):
        """
        Returns True if res is properly formatted and False otherwise.
        Runtime: O(N), Space: O(1)
        """
        last_a = -1
        first_b = len(res)
        for i, char in enumerate(res):
            if char == 'A':
                last_a = i
            elif char == 'B' and first_b == len(res):
                first_b = i
            if last_a > first_b:
                return False
        return True

    def delete_letter(start, result, seen):
        """
        Returns the minimum number of letters that need to be deleted from s to achieve a properly formatted string.
        """
        if start >= len(s):
            if result in seen:
                return len(s) - len(result)
            if is_valid(result):
                seen.add(result)
                return len(s) - len(result)
            return len(s)
        return min(delete_letter(start + 1, result + s[start], seen), delete_letter(start + 1, result, seen))

    if is_valid(s):
        return 0
    return delete_letter(0, '', set())


def min_deletions_other(s):
    """
    Runtime: O(N), Space: O(1)
    """
    last_a = -1
    first_b = len(s)
    for i, char in enumerate(s):
        if char == "A":
            last_a = i
        elif char == "B" and first_b == len(s):
            first_b = i

    count_a_after_first_b = 0
    count_b_before_last_a = 0
    for i, char in enumerate(s):
        if char == "A" and i > first_b:
            count_a_after_first_b += 1
        elif char == "B" and i < last_a:
            count_b_before_last_a += 1
    print(count_a_after_first_b, count_b_before_last_a)
    return min(count_a_after_first_b, count_b_before_last_a)


def test(function):
    assert function('BAAABAB') == 2
    assert function('BBABAA') == 3
    assert function("AABBBB") == 0
    assert function("BAB") == 1
    assert function("BABABABA") == 4
    assert function("AAAABABAAAA") == 2


functions = [min_deletions_naive, min_deletions_other]
for func in functions:
    test(func)
