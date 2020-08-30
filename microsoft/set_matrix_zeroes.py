"""
Source: Leetcode
Input: 2D array of integers
Output: Modify in-place. Find each zero in the array and zero out its row and column

Runtime: O(mn) for an m x n array
Space complexity naive: O(m + n)
Space complexity optimal: O(1)

Example
Input: [
    [1, 2, 3, 0, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
]
Output: [
    [0, 0, 0, 0, 0, 0],
    [1, 2, 3, 0, 5, 6],
    [1, 2, 3, 0, 5, 6]
]

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Idea O(m + n) space
- Iterate through the matrix once, keep track of the rows and columns where there's a zero in two sets: one for rows, one
  for cols
- Iterate through the matrix again. If the row or column is in the previous sets, change the element of the matrix to zero

O(1) space solution
- use the first cell of every row and column as a flag. If first cell of a row is set to zero then row should be changed
  to zero. Same for column
- first cell of row 0 and first cell of col 0 are both the same cell matrix[0][0], so we need an additional flag for
  either the first row or col. Let's say first col, so the flag could be set_first_col. Then, matrix[0][0] would be used
  to indicate that the first row needs to be set to zero.

- iterate through the matrix. If an element is zero, set the first cell in its row to zero and the first cell in its col
  to zero
    - if we need the first column of the matrix to be zero, set set_first_col to True
- iterate through matrix again but start at row 1 and col 1.
  If matrix[i][0] for each row i is zero or matrix[0][j] is zero for each col j, then set matrix[i][j] to zero

- first row and col are treated as a special case because of matrices like this
  [
    [1, 1, 1],
    [0, 1, 2],
  ]
  where we'd mark matrix[0][0] as zero if we didn't consider it a special case, which would cause all of row 0 to be
  changed to zero
- look at matrix[0][0] and set the corresponding zeros last because otherwise all of row 0 and all of col 0 would be
  zero and we'd end up setting the entire matrix to zero
"""


def set_matrix_zeroes_alt(matrix):
    """
    Source: Leetcode
    Runtime: O(mn) for an m x n array
    Space complexity: O(1)
    """
    if not matrix:
        return

    m, n = len(matrix), len(matrix[0])
    set_first_col = False
    for i in range(m):
        if matrix[i][0] == 0 and not set_first_col:
            set_first_col = True

        for j in range(1, n):
            # set the first element of this row and first element of this col to zero
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            # set all elements in this row and all elements in this col to zero
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    # set each element of the first row to zero
    if matrix[0][0] == 0:
        # matrix[0][0] acts as set_first_row flag
        for j in range(n):
            matrix[0][j] = 0

    # set each element of the first column to zero
    if set_first_col:
        for i in range(m):
            matrix[i][0] = 0

    print(matrix)


def set_matrix_zeroes(matrix):
    """
    Runtime: O(mn) for an m x n array
    Space complexity: O(m + n)
    """
    if not matrix:
        return

    rows, cols = set(), set()
    num_rows, num_cols = len(matrix), len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(num_rows):
        if i in rows:
            matrix[i] = [0] * num_cols
            continue
        for j in range(num_cols):
            if j in cols:
                matrix[i][j] = 0
    print(matrix)


set_matrix_zeroes([
    [1, 2, 3, 0, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
])

set_matrix_zeroes([])

set_matrix_zeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
])

set_matrix_zeroes_alt([
    [1, 2, 3, 0, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
])
set_matrix_zeroes_alt([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
])
