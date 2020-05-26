"""
Input: string s and length n
Output: number of occurrences of a in the prefix of length n in the infinitely repeating string
"""


def repeated_string(s, n):
    full_repeats = n // len(s)
    partial = n % len(s)
    return s.count("a") * full_repeats + s[:partial].count("a")
