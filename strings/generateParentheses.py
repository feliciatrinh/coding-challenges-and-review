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


def genParentheses(n):
    result = []
    if n < 1:
        return result

    def combine(curr, numOpen, numClosed):
        if numOpen + numClosed == 2 * n:
            result.append(curr)
            return

        if numOpen < n:
            combine(curr + '(', numOpen + 1, numClosed)

        if numClosed < numOpen:
            combine(curr + ')', numOpen, numClosed + 1)

    combine("", 0, 0)
    return result


assert genParentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
