"""
Source: Linkedin learning
Input: positive integer
Output: prime factorization as a list

Example
Input: 60
Output: [2, 2, 3, 5]
"""


def prime_factorization(x):
    result = []
    divisor = 2
    while x > 1 and divisor <= x:
        if x % divisor == 0:
            result.append(divisor)
            x = x // divisor
        else:
            divisor += 1
    return result


print(prime_factorization(60))
