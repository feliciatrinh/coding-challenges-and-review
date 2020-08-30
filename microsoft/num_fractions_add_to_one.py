"""
Given N fractions.
Fractions rep'd as two arrays, X and Y of length N, containing the numerators and denoms respectively

Write func that given arrays X and Y of length N, returns num of possible ways to choose a pair of fractions that sum to
1. This answer can be large, so provide it modulo 10^9 + 7 (1000000007).

A single fraction can form multiple pairs.

0 <= N <= 100,000
Each element in X and Y are in range [1, 10^9]

Example
Input: X = [1, 1, 2], Y = [3, 2, 3]
Output: 1
Explanation: fractions are (1/3, 1/2, 2/3) only pair that sums to 1 is (1/3, 2/3)

Input: X = [1, 1, 1], Y = [2, 2, 2]
Output: 3
Fractions are (1/2, 1/2, 1/2). 3 ways to choose a pair that sums to 1

Input: X = [1, 2, 3, 1, 2, 12, 8, 4], Y = [5, 10, 15, 2, 4, 15, 10, 5]
Output: 10

Idea
- solve it like the two sum problem
- iterate through the reduced version of each fraction
    - calculate the complement
    - if you've seen the complement before, increment the count of pairs that sum to 1 by the frequency of the
      complement
    - can use collections.Counter to keep track of frequencies concisely
- fractions can't be negative, so if the numerator > denominator (aka any fraction is already greater than 1) you can
  continue onto the next fraction
"""


def gcd(a, b):
    """
    Return the greatest common divisor (aka greatest common factor) between a and b.
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def reduce(numer, denom):
    gcf = gcd(numer, denom)
    return numer // gcf, denom // gcf


def add_fraction_general(frac_a, frac_b):
    """
    How to add two fractions and reduce to lowest terms in general. Makes the numerator negative if the
    fraction is negative by convention.
    """
    num_a, denom_a = frac_a
    num_b, denom_b = frac_b

    lcm = denom_a * denom_b // gcd(denom_a, denom_b)
    num_a *= lcm // denom_a
    num_b *= lcm // denom_b
    num_res = num_a + num_b
    sign = -1 if num_res < 0 else 1
    re_num, re_denom = reduce(sign * num_res, lcm)
    return sign * re_num, re_denom


def num_fractions(X, Y):
    """
    Runtime: O(n), Space Complexity: O(n)
    """
    def whole_num_sub_frac(whole_num, frac_b):
        """
        Returns result of subtracting a fraction from a whole number as a fraction. Makes the numerator negative if the
        fraction is negative by convention.
        """
        num_a, denom_a = whole_num, whole_num
        num_b, denom_b = frac_b
        lcm = denom_b

        num_a *= lcm
        num_res = num_a - num_b
        sign = -1 if num_res < 0 else 1
        re_num, re_denom = reduce(sign * num_res, lcm)
        return sign * re_num, re_denom

    if not X or not Y:
        return 0

    m = 1000000007
    count = 0
    seen = dict()
    for i in range(len(X)):
        numer, denom = reduce(X[i], Y[i])
        # this fraction is greater than or equal to 1
        if numer >= denom:
            continue
        # add_fraction_general() and whole_num_sub_frac() both work here
        # complement = add_fraction_general((1, 1), (-numer, denom))
        complement = whole_num_sub_frac(1, (numer, denom))
        if complement in seen:
            count += seen[complement]
        if (numer, denom) in seen:
            seen[(numer, denom)] += 1
        else:
            seen[(numer, denom)] = 1
    return count % m


assert num_fractions([1, 1, 2], [3, 2, 3]) == 1
assert num_fractions([1, 1, 1], [2, 2, 2]) == 3
assert num_fractions([1, 2, 3, 1, 2, 12, 8, 4], [5, 10, 15, 2, 4, 15, 10, 5]) == 10
assert num_fractions([5, 6, 5], [11, 11, 11]) == 2
