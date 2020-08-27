"""
Source: Leetcode
Input: integer n
Output: any array containing n unique integers that add up to 0

Example
Input: 5
Output: [-2, -1, 0, 1, 2] is a possible answer
"""


def array_zero(n):
    if n % 2 != 0:
        result = [0]
        n -= 1
    else:
        result = []

    start = 1
    curr_sum = 0
    for i in range(n):
        if curr_sum <= 0:
            result.append(start)
            curr_sum += start
        else:
            result.append(-start)
            curr_sum -= start
            start += 1
    return result


assert sum(array_zero(5)) == 0
assert sum(array_zero(3)) == 0
assert sum(array_zero(1)) == 0
