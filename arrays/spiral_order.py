"""
Source: Leetcode
Input: m x n matrix
Output: all elements of the matrix in spiral order

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Idea:
- Remove the top and right layer of the matrix and add it to your spiral
- Remove the bottom and left layer of the matrix and add it to your spiral
- Repeat until there is only one element remaining in the matrix
- This works b/c you mutate the matrix as you go along
"""


def spiral_order(matrix):
    """
    Return the matrix in spiral order as a single list.
    """

    def layer_top_right(matrix):
        """
        Return the top row and right column of the matrix.
        """
        top = matrix.pop(0)
        # for row in matrix:
        #     if len(row) == 1:
        #         return top + 
        right = [row.pop() for row in matrix if row]
        return top + right

    def layer_bottom_left(matrix):
        """
        Return the bottom row and left column of the matrix in the order of the spiral.
        """
        bottom = matrix.pop()
        left = [row.pop(0) for row in matrix if row]
        return bottom[::-1] + left[::-1]

    spiral = []

    while matrix:
        if len(matrix) == 1:
            spiral += matrix[0]
            break

        spiral += layer_top_right(matrix)
        spiral += layer_bottom_left(matrix)

    return spiral


matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

assert spiral_order(matrix_1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order(matrix_2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_order([[7], [9], [6]]) == [7, 9, 6]
