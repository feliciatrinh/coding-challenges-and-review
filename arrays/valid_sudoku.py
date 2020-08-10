"""
Source: Leetcode
Input: List of lists containing digits 1-9 as strings and the character '.' representing a 9 x 9 board
Output: boolean indicating whether Sudoku board is valid

Runtime: O(n^2)?
Space complexity: O(n^2)?

Only filled cells need to be validation according to these rules:
1. Each row must contain digits 1-9 w/o repetition
2. Each col must contain digits 1-9 w/o rep
3. Each of the 9 3x3 sub-boxes must contain digits 1-9 w/o rep

Example 1
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false

Ideas
- could iterate through each row then each column then each sub-box and keep track of whether it satisfies the rules
    - inefficient: looks at the same element multiple times
- extra space: needs at least one extra data structure like a set to keep track of the elements
    - could use a nested dictionary to avoid looking at the same element multiple times
    {row: {0: set(), 1: set(), ..., 8: set()},
     col: {0: set(), 1: set(), ..., 8: set()},
     box: {0: set(), 1: set(), ..., 8: set()}
     }
    - fill in the dictionary as you scan through each row
    - can fill in the box dictionary by calculating which box the digit is in based on the given row and col
        - TODO: try to calculate which box the digit is in using math instead of many if statements
"""


def naive_valid_sudoku(board):
    def identify_box(row, col):
        if row < 3:
            if col < 3:
                return 0
            elif 3 <= col <= 5:
                return 1
            elif 6 <= col <= 8:
                return 2
        elif 3 <= row <= 5:
            if col < 3:
                return 3
            elif 3 <= col <= 5:
                return 4
            elif 6 <= col <= 8:
                return 5
        elif 6 <= row <= 8:
            if col < 3:
                return 6
            elif 3 <= col <= 5:
                return 7
            elif 6 <= col <= 8:
                return 8

    log = dict(row={i: set() for i in range(9)}, col={i: set() for i in range(9)}, box={i: set() for i in range(9)})
    for row in range(9):
        for col in range(9):
            element = board[row][col]
            if element == ".":
                continue
            box = identify_box(row, col)
            if element in log["row"][row] or element in log["col"][col] or element in log["box"][box]:
                return False
            else:
                log["row"][row].add(element)
                log["col"][col].add(element)
                log["box"][box].add(element)
    return True


assert naive_valid_sudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]) is True
assert naive_valid_sudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]) is False
