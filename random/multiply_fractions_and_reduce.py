"""
Input: list of Fraction objects
Output: the product in reduced form

A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.
class fractions.Fraction(numerator=0, denominator=1)

The Fraction type has a __mul__() method, which takes two Fractions and returns a Fraction as a result. It will
always return the simplest (lowest common denominator) version of the faction. 
"""


def multiply_fractions_and_reduce(lst):
    product = reduce(lambda x, y: x * y, fracs)
    return product.numerator, product.denominator
