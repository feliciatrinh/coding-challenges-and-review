"""
Input: string containing an infix mathematical expression
Output: answer to the expression

Runtime: O(n)

Assume each expression is well-formed/valid.

Infix: A + B, A + B * C
Prefix: + A B, + A * B C
Postfix: A B +, A B C * +

Example
Input: "3+2-1"
Output: 4
"""


def eval_wo(expression):
    """
    Solve without using built-in functions like replace or using regex.
    Expression can be empty string. Spacings aren't standardized. Only have positive integers.
    Examples: " 3     + 1-9" outputs -5

    Runtime: O(n)
    Space complexity: O(1)
    """
    if not expression:
        return 0

    result = 0
    operators = {"+", "-"}
    number = ""
    op = ""
    for char in expression:
        if char == " ":
            continue
        elif char in operators:
            result += int(op + number)
            number = ""
            op = char
        else:
            number += char
    result += int(op + number)
    return result


def eval_wo_alt(expressions):
    """
    Solve without using built-in functions like replace or using regex.
    Expression can be empty string. Spacings aren't standardized. Only have positive integers.
    Examples: " 3     + 1-9" outputs -5

    Runtime: O(n)
    Space complexity: O(n)
    """
    if not expressions:
        return 0

    valid_operators = {"+", "-"}
    numbers = []
    operators = []
    num = ""
    for char in expressions:
        if char == " ":
            continue
        elif char in valid_operators:
            operators.append(char)
            numbers.append(num)
            num = ""
        else:
            num += char
    numbers.append(num)

    result = int(numbers.pop(0))
    while numbers:
        result += int(operators.pop(0) + numbers.pop(0))
    return result


def eval_add_sub_regex(expression):
    """
    Treat subtractions as negative integers and additions as positive integers then sum all of the integers together.
    """
    import re

    if not expression:
        return 0

    expression = expression.replace(" ", "")
    nums_str = re.findall(r'\-?\d+', expression)
    nums = map(int, nums_str)
    return sum(nums)


def eval_all_ops_alt(expression):
    """
    Infix Evaluation
    Solve expression containing +, -, *, / taking care of order of operations.
    Expression can be empty string. Spacings aren't standardized. Only have positive integers.

    Runtime: O(n)
    Space complexity: O(n)
    """
    def evaluate(num1, num2, op):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2

    if not expression:
        return 0

    num_stack = []
    op_stack = []
    priority = {"*", "/"}
    operators = {"+", "-", "*", "/"}
    number = ""
    for char in expression:
        if char == " ":
            continue
        elif char in operators:
            if op_stack and op_stack[-1] in priority:
                num_stack.append(evaluate(num_stack.pop(), int(number), op_stack.pop()))
            else:
                num_stack.append(int(number))
            op_stack.append(char)
            number = ""
        else:
            number += char
    num_stack.append(int(number))

    while op_stack:
        second = num_stack.pop()
        num_stack.append(evaluate(num_stack.pop(), second, op_stack.pop()))
    return num_stack[0]


def eval_all_ops(expression):
    """
    First attempt
    Solve expression containing +, -, *, / taking care of order of operations.
    Expression can be empty string. Spacings aren't standardized. Only have positive integers.

    Runtime: O(n)
    Space complexity: O(n)
    """
    if not expression:
        return 0

    num_stack = []
    op_stack = []
    operators = {"+", "-", "*", "/"}
    priority = {"*", "/"}
    number = ""
    for char in expression:
        if char == " ":
            continue
        elif char in operators:
            if op_stack and op_stack[-1] in priority:
                if op_stack[-1] == "*":
                    result = num_stack.pop() * int(number)
                elif op_stack[-1] == "/":
                    result = num_stack.pop() / int(number)
                op_stack.pop()
                num_stack.append(result)
            else:
                num_stack.append(int(number))
            number = ""
            op_stack.append(char)
        else:
            number += char

    if op_stack and op_stack[-1] in priority:
        if op_stack[-1] == "*":
            result = num_stack.pop() * int(number)
        elif op_stack[-1] == "/":
            result = num_stack.pop() / int(number)
        op_stack.pop()
        num_stack.append(result)
    else:
        num_stack.append(int(number))

    result = num_stack.pop(0)
    for i in range(len(op_stack)):
        op = op_stack[i]
        num = num_stack[i]
        if op == "+":
            result += num
        elif op == "-":
            result -= num
    return result


def eval_add_sub(expression):
    """
    Old solution
    """
    if not expression:
        return 0

    expression = expression.replace(" ", "")
    result = int(expression[0])
    for i in range(1, len(expression), 2):
        op, num = expression[i: i + 2]
        if op == "+":
            result += int(num)
        elif op == "-":
            result -= int(num)
    return result


assert eval_add_sub("3+2-1") == 4
assert eval_add_sub("0 - 4 - 2") == -6
assert eval_add_sub("0 -4- 2") == -6
assert eval_add_sub("7") == 7

assert eval_add_sub_regex("3+2-1") == 4
assert eval_add_sub_regex("0 - 4 - 2") == -6
assert eval_add_sub_regex("0 -4- 2") == -6
assert eval_add_sub_regex("7") == 7
assert eval_add_sub_regex("-7-9+11") == -5

assert eval_wo("  3      + 10-9") == 4
assert eval_wo("5") == 5

assert eval_wo_alt("  3      + 10-9") == 4
assert eval_wo_alt("5") == 5

assert eval_all_ops_alt("1 + 4*5 - 2") == 19
assert eval_all_ops_alt("   2 / 2  -1 * 4  /2 ") == -1
