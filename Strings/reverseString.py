def reverseString(s):
    """
    Given a string s, return the verse of the string.
    O(n) runtime? 
    """
    return s[::-1]

def reverseString2(s):
    """
    recursive solution
    """
    if len(s) == 1:
        return s
    return reverseString2(s[1:]) + s[0]
