"""
Source: Leetcode
Input: String describing an expression that adds or subtracts fractions, fractions will be in the form of a/b where a and b are
       integers and cannot be zero
Output: String of the sum in lowest terms

Runtime: O(n)

Note: fractions can be negative

Example
Input: "1/4 + 1/6"
Output: "5/12"

Example
Input: "-1/2+1/2+1/3"
Output: "1/3"
"""


def add_sub_fracs_and_reduce(expression):
    import re
    from fractions import Fraction

    frac_strings = re.findall(r'\-?\d+\/\d+', expression)
    fracs = map(Fraction, frac_strings)
    result = sum(fracs)
    return "{}/{}".format(result.numerator, result.denominator)


#########################################################################
###### PAST SOLUTIONS AND SLIGHT PROBLEM VARIATIONS ARE FOUND BELOW #####
#########################################################################

def add_fracs_and_reduce_string_better(expression):
    """
    Alternative solution that uses the built in fractions.Fraction class.
    Assumes addition of only two fractions.
    """
    from fractions import Fraction

    first_frac, second_frac = map(Fraction, expression.split("+"))
    result = first_frac + second_frac
    return "{}/{}".format(result.numerator, result.denominator)


assert add_fracs_and_reduce_string_better("722/148+360/176") == "2818/407"


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def add_fracs_and_reduce_string(expression):
    """ Assumes addition of only two fractions. """
    import re

    numerators = re.findall(r'(\d+)\/', expression)
    denominators = re.findall(r'\/(\d+)', expression)

    numer1, numer2 = int(numerators[0]), int(numerators[1])
    denom1, denom2 = int(denominators[0]), int(denominators[1])

    # find the least common multiple
    lcm = denom1 * denom2 // gcd(denom1, denom2)
    numer_sum = numer1 * lcm // denom1 + numer2 * lcm // denom2

    # reduce to lowest terms
    greatest_common_factor = gcd(numer_sum, lcm)
    num = numer_sum // greatest_common_factor
    denom = lcm // greatest_common_factor
    return "{}/{}".format(num, denom)


assert add_fracs_and_reduce_string("12/14 + 1/14") == "13/14"
assert add_fracs_and_reduce_string("3/4 + 2/5") == "23/20"
assert add_fracs_and_reduce_string("1/2 + 5/14") == "6/7"
assert add_fracs_and_reduce_string("722/148+360/176") == "2818/407"


# Input: list of numerators, list of denominators (both lists are the same length, both contain integers)
#        representing fractions
# Output: tuple of numerator and denominator of sum of the fractions in reduced form

# Assume input cannot be empty.

# - to add two fractions, you need to find the LCM of the two denominators
# - LCM * GCD = x * y so you can solve for the LCM after finding the GCD


def add_fractions_and_reduce(numerators, denominators):
    """
    Iterative solution
    """
    while len(numerators) > 1 and len(denominators) > 1:
        numer1, numer2 = numerators[0], numerators[1]
        denom1, denom2 = denominators[0], denominators[1]

        lcm = denom1 * denom2 // gcd(denom1, denom2)
        numer_sum = numer1 * lcm // denom1 + numer2 * lcm // denom2

        # Reduce the fraction to its lowest terms and replace the two fractions with its sum
        greatest_common_factor = gcd(numer_sum, lcm)
        numerators[:2] = [numer_sum // greatest_common_factor]
        denominators[:2] = [lcm // greatest_common_factor]

    return numerators[0], denominators[0]


assert add_fractions_and_reduce([1, 1], [4, 3]) == (7, 12)
assert add_fractions_and_reduce([2, 4], [4, 6]) == (7, 6)
assert add_fractions_and_reduce([1, 1, 2], [5, 1, 3]) == (28, 15)


def add_fractions_and_reduce_recursive(numerators, denominators):
    """
    Recursive solution
    """
    if len(numerators) > 1 and len(denominators) > 1:
        numer1, numer2 = numerators[0], numerators[1]
        denom1, denom2 = denominators[0], denominators[1]

        lcm = denom1 * denom2 // gcd(denom1, denom2)
        numer_sum = numer1 * lcm // denom1 + numer2 * lcm // denom2

        # Reduce the fraction to its lowest terms and replace the two fractions with its sum
        greatest_common_factor = gcd(numer_sum, lcm)
        numerators[:2] = [numer_sum // greatest_common_factor]
        denominators[:2] = [lcm // greatest_common_factor]

        return add_fractions_and_reduce_recursive(numerators, denominators)

    return numerators[0], denominators[0]


assert add_fractions_and_reduce_recursive([1, 1], [4, 3]) == (7, 12)
assert add_fractions_and_reduce_recursive([2, 4], [4, 6]) == (7, 6)
assert add_fractions_and_reduce_recursive([1, 1, 2], [5, 1, 3]) == (28, 15)
