"""
Source: Leetcode
Input: array of characters
Output: None

Runtime: O(n)
Space: O(1)

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

- we can just use .reverse() as a one-liner solution, but that's boring.
"""


def reverse(s):
    """
    Reverse a list in-place using two pointers.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s1 = ["a", "p", "p", "l", "e"]
reverse(s1)
assert s1 == ["e", "l", "p", "p", "a"]


# If our problem statement was to return a new list that was the reverse of the first, we could do the following
def reverse_alt(s):
    return s[::-1]


def reverse_alt_2(s):
    """
    Recursive solution.
    """
    if len(s) < 2:
        return s
    return reverse_alt_2(s[len(s) // 2:]) + reverse_alt_2(s[:len(s) // 2])


assert reverse_alt_2(["a", "p", "p", "l", "e"]) == ["e", "l", "p", "p", "a"]
