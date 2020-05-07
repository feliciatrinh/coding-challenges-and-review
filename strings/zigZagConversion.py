"""
Source: LeetCode
Input: string s, numRows
Output: string after zig zag conversion

Runtime: O(n)?

General strategy: 
- write down the indices of each letter in the zig zag pattern
- the first follows the same pattern of every 2*(numRows - 1)-th letter
  starting from the 0th letter
- middle rows alternate between adding n or m to the index of the letter that
  you add to result
    - n starts as 2 * (numRows - 2)
    - m starts as 2
- n decreases by 2 and m increases by 2 when you proceed to the next row
- last row follows pattern of every 2*(numRows - 1)-th letter
  starting from the (numRows - 1)th letter

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

0   4   8   12
1 3 5 7 9 11 13
2   6   10

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

0     6    12
1   5 7  11 13
2 4   8 10
3     9

Example 3:
Input: s = "PAYPALISHIRING", numRows = 5
Output: "PHASIYIRPLIGAN"

P       H    
A     S I  
Y   I   R 
P L     I G
A       N
"""


def convert(s: str, numRows: int) -> str:
    def alternate(n, m, flag):
        """
        Generator that yields n or m depending on the flag
        """
        if flag:
            yield n
            flag = False
        else:
            yield m
            flag = True

    if numRows < 2:
        return s

    s_list = list(s)
    # append every 2 * (numRows - 1) letter for row 0
    result = s_list[::2 * (numRows - 1)]

    # the middle rows follow a different pattern
    start_index = 1
    flag = True
    n = 2 * (numRows - 2)
    m = 2
    while start_index < numRows - 1:
        curr_index = start_index
        # gen_flag is used to alternate between yielding n or m
        gen_flag = flag
        while curr_index < len(s):
            result.append(s_list[curr_index])
            curr_index += next(alternate(n, m, gen_flag))
            gen_flag = not gen_flag
        n -= 2
        m += 2
        start_index += 1

    # append every 2 * (numRows - 1) letter for last row
    result += s_list[start_index::2 * (numRows - 1)]
    return ''.join(result)

assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
