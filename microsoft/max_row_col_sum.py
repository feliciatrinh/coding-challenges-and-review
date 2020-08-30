"""
Input: matrix as a 2D array with row and col size given
Output: sum of the maximum row sum and maximum column sum i.e. max_row_sum + max_col_sum

I'm going to assume matrix is always a valid input.
"""


def max_sum(matrix, m, n):
    """
    Runtime: O(m * n), Space: O(1)
    """
    max_row_sum = sum(matrix[0])
    max_col_sum = matrix[0][0]
    for i in range(1, m):
        max_row_sum = max(max_row_sum, sum(matrix[i]))
        max_col_sum += matrix[i][0]

    for j in range(1, n):
        col_sum = 0
        for i in range(m):
            col_sum += matrix[i][j]
        max_col_sum = max(max_col_sum, col_sum)
    return max_row_sum + max_col_sum


assert max_sum([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 3, 4) == 7
assert max_sum([[-2], [-1], [-3], [1]], 4, 1) == -4
assert max_sum([[5]], 1, 1) == 10
