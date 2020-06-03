"""
Source: Leetcode
Input: integer n
Output: list of string representations of numbers from 1 to n, but for multiples of 3 it should output "Fizz" instead of
        the number. For multiples of five, it should output "Buzz". For multiples of both, it should output "FizzBuzz."

Runtime: O(n)
Space: O(n)
"""


def fizz_buzz(n):
    result = []
    for num in range(1, n + 1):
        if num % 5 == 0 and num % 3 == 0:
            result.append("FizzBuzz")
        elif num % 5 == 0:
            result.append("Buzz")
        elif num % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(num))
    return result


def fizz_buzz_alt(n):
    result = []
    for num in range(1, n + 1):
        str_rep = ""
        if num % 3 == 0:
            str_rep += "Fizz"
        if num % 5 == 0:
            str_rep += "Buzz"
        if not str_rep:
            str_rep = str(num)
        result.append(str_rep)
    return result


def fizz_buzz_alt_2(n):
    """ Source: Leetcode """
    result = [str(num) for num in range(1, n + 1)]
    for i in range(2, n, 3):
        result[i] = "Fizz"
    for i in range(4, n, 5):
        result[i] = "Buzz"
    for i in range(14, n, 15):
        result[i] = "FizzBuzz"
    return result


assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
assert fizz_buzz_alt(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
assert fizz_buzz_alt_2(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
