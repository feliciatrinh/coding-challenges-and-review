"""
Source: leedcode
Input: n, the number of pairs of parentheses
Output: list of all valid combinations of well-formed parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example
Input: n=3
Output: [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

- Keep track of the number of open and closed parentheses
- Only add an open parenthesis when there are any left out of the n
- Add a closed parenthesis if the number of closed parentheses does not exceed
  the current number of open parentheses
"""


def gen_parentheses(n):
    result = []
    if n < 1:
        return result

    def combine(curr, num_open, num_closed):
        if num_open + num_closed == 2 * n:
            result.append(curr)
            return

        if num_open < n:
            combine(curr + '(', num_open + 1, num_closed)

        if num_closed < num_open:
            combine(curr + ')', num_open, num_closed + 1)

    combine("", 0, 0)
    return result


assert gen_parentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
