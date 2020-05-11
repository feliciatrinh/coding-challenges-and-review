"""
Input: string consisting only of '(', ')', '{', '}', '[' and ']'
Output: True if characters are balanced, False otherwise

Empty string counts as True.

Runtime: O(n)
"""


def isValid(s: str) -> bool:
    if not s:
        return True
    
    open_chars = {'(', '{', '['}
    closed_open = {')': '(', '}': '{', ']': '['}
    
    stack = []
    for letter in s:
        if letter in open_chars:
            stack.append(letter)
        elif letter in closed_open.keys():
            if not stack:
                return False

            top = stack.pop()
            if top != closed_open[letter]:
                return False

    if not stack:
        return True


assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([)]") == False
assert isValid("{[]}") == True
