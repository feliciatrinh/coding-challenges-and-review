"""
Source: hackerrank, geeksforgeeks
Input: string s
Output: list of all possible substrings of s

Runtime: approx O(n^2)

Example 1:
Input: "Geeks"
Output: [‘G’, ‘Ge’, ‘Gee’, ‘Geek’, ‘Geeks’, ‘e’, ‘ee’, ‘eek’, ‘eeks’, ‘e’, ‘ek’, ‘eks’, ‘k’, ‘ks’, ‘s’]
"""
from itertools import combinations


def bruteforce_substrings(s):
    """
    Runtime: O(n^2)
    """
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def combinations_substrings(s):
    """
    Runtime: O(r * n! / ((n - r)! * r!)) aka O(r * (n choose r))
    itertools.combinations(iterable, r) returns r length subsequences of
    elements from the input
    """
    return [s[i:j] for i, j in combinations(range(len(s) + 1), 2)]
