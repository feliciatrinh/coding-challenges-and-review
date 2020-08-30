"""
Input: sequence of operations as a string
Output: topmost value from the stack after all of the operations have been done or -1 if the machine would report an
        error.

Operations possible, each separated by a space:
- integer X from 0 to 2^20 - 1: machine pushes X onto the stack
- "POP": machine removes topmost num from stack
- "DUP": machine pushes a duplicate of topmost num onto stack
- "+": machine pops two topmost elements from stack, adds them together, and pushes sum onto stack
- "-": pops two topmost elements, subtracts the second one from the first (topmost), pushes difference onto stack

Rules:
- 20-bit unsigned integers (from 0 to 2^20 - 1)
- overflow in addition or underflow in subtraction causes error
- error when tries to perform operation that expects more nums on stack than stack contains (e.g. pop but stack is empty)
- error if stack empty after performing all operations

Assume len(s) in range [0, 2000]
S is a valid sequence of word machine operations

Example
Input: "13 DUP 4 POP 5 DUP + DUP + -"
Output: 7
Stack initially empty
13
13 13
13 13 4
13 13
13 13 5
13 13 5 5
13 13 10
13 13 10 10
13 13 20
13 7

Input: "5 6 + -"
Output: -1 aka error
Stack initially empty
5
5 6
11
there needs to be 2 nums on the stack to subtract

Input: "3 DUP 5 - -"
Output:
Stack initially empty
3
3 3
3 3 5
3 2
-1 (is this an underflow?)
"""


def word_machine(s):
    """
    Written for correctness only
    Runtime: O(n), space complexity: O(n)
    """
    stack = []
    op = ''
    for i in range(len(s) + 1):
        if (i == len(s) and op) or s[i] == ' ':
            if op == "POP":
                if not stack:
                    return -1
                stack.pop()
            elif op == "DUP":
                if not stack:
                    return -1
                stack.append(stack[-1])
            elif op == "+":
                if len(stack) < 2:
                    return -1
                result = stack.pop() + stack.pop()
                if result > 2**20 - 1:
                    return -1
                stack.append(result)
            elif op == "-":
                if len(stack) < 2:
                    return -1
                result = stack.pop() - stack.pop()
                if result < 0:
                    return -1
                stack.append(result)
            else:
                stack.append(int(op))
            op = ''
        else:
            op += s[i]

    if not stack:
        return -1
    return stack[-1]


def word_machine_alt(s):
    """
    Runtime: O(n), space complexity: O(n)
    """
    stack = []
    op = ''
    for i in range(len(s) + 1):
        if (i == len(s) and op) or s[i] == ' ':
            if op == "POP" or op == "DUP":
                if not stack:
                    return -1
                if op == "POP":
                    stack.pop()
                elif op == "DUP":
                    stack.append(stack[-1])
            elif op == "+" or op == "-":
                if len(stack) < 2:
                    return -1
                if op == "+":
                    result = stack.pop() + stack.pop()
                elif op == "-":
                    result = stack.pop() - stack.pop()
                if result < 0 or result > 2**20 - 1:
                    return -1
                stack.append(result)
            else:
                stack.append(int(op))
            op = ''
        else:
            op += s[i]

    if not stack:
        return -1
    return stack[-1]


assert word_machine("13 DUP 4 POP 5 DUP + DUP + -") == 7
assert word_machine("5 6 + -") == -1
assert word_machine("3 DUP 5 - -") == -1

assert word_machine_alt("13 DUP 4 POP 5 DUP + DUP + -") == 7
assert word_machine_alt("5 6 + -") == -1
assert word_machine_alt("3 DUP 5 - -") == -1
