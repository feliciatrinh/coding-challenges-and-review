"""
Input: a postfix mathematical expression in the form of a string made of single-digit operands and 4 operators
Output: answer to the expression

Infix: A + B, A + B * C
Prefix: + A B, + A * B C
Postfix: A B +, A B C * +

- if operands weren't single digit, you'd just need to build up the operand by taking advantage of the spaces
- assuming input expression is a valid expression
- not going to assume any uniformity in spaces
"""


def postfix_evaluation(expression):
    """
    Runtime: O(N), Space: O(N)
    """
    def evaluate(num1, num2, op):
        if op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        elif op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2

    if not expression:
        return 0

    ops = {'*', '/', '+', '-'}
    nums_stack = []
    for char in expression:
        if char == ' ':
            continue
        elif char in ops:
            num2 = nums_stack.pop()
            nums_stack.append(evaluate(nums_stack.pop(), num2, char))
        else:
            nums_stack.append(int(char))
    return nums_stack[0]


assert postfix_evaluation('2   3 1 * +    9 -') == -4
assert postfix_evaluation('1    2 + 2 * 5 -    9 * 3 /') == 3
assert postfix_evaluation('5  ') == 5

