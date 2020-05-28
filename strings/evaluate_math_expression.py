"""
Input: string containing a mathematical expression
Output: answer to the expression

Runtime: O(n)

Assume each expression is well-formed/valid and it can't be the empty string.
Using *, /, and parentheses gets complex b/c of precedence so let's deal with + and - first.
I'm not going to assume the presence or lack of white spaces.

Example
Input: "3+2-1"
Output: 4

TODO: solve expression containing * and / as well
"""


def eval_add_sub_better(expression):
    """
    Treat subtractions as negative integers and additions as positive integers then sum all of the integers together.
    """
    import re

    expression = expression.replace(" ", "")
    nums_str = re.findall(r'\-?\d+', expression)
    nums = map(int, nums_str)
    return sum(nums)


def eval_add_sub(expression):
    """
    Old solution
    """
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

assert eval_add_sub_better("3+2-1") == 4
assert eval_add_sub_better("0 - 4 - 2") == -6
assert eval_add_sub_better("0 -4- 2") == -6
assert eval_add_sub_better("7") == 7
assert eval_add_sub_better("-7-9+11") == -5
