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

def eval_add_sub(expression):
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
