"""
Source: Leetcode
Input: m, number of rows and n, number of columns for your m x n matrix
Output: total number of paths from the top left corner to the bottom right corner

Runtime: O(m * n)
Space Complexity: O(m * n) can be reduced to O(n) because each row is used only once in recurrence relation

You may only move down or to the right.

Example:
Input:
[[1, 2, 3], 
 [4, 5, 6],
 [7, 8, 9]]
Output: 6

Explanation: has paths
[1, 4, 7, 8, 9]
[1, 4, 5, 8, 9]
[1, 4, 5, 6, 9]
[1, 2, 5, 8, 9]
[1, 2, 5, 6, 9]
[1, 2, 3, 6, 9]

SOLUTION 1
Runtime: O(m * n), Space Complexity: O(m * n)

Subproblem:
P(i, j) is the total number of paths that pass through (i, j).

Base Case: P(0, 0) = 1

Recurrence Relation: P(i, j) = P(i - 1, j) + P(i, j - 1)
- Add up the paths from the cell above you and the cell to the left of you because you moved either down or right to get
  to the current cell


BETTER SOLUTION
Runtime: O(m * n), Space Complexity: O(n)

Idea
- You only need to use each row once, so there's no need to keep track of the entire matrix
- You can simply write over the same list at each iteration

Subproblem:
P(j) is the total number of paths that pass through column j at iteration i

Base case: P(0) = 1 for all i

Recurrence Relation: P(j) = P(j) + P(j - 1)
- You only need to add the number of paths from the cell to your left

Example
Input: m=4, n=3
Output: 10

Grid for Space Complexity O(mn)
[[1, 1, 1, 1]
 [1, 2, 3, 4],
 [1, 3, 6, 10]]

 The top row and left column are always ones.

 Grid for Space Complexity O(n)
 i = 0: [1, 1, 1, 1]
 i = 1: [1, 2, 3, 4]
 i = 2: [1, 3, 6, 10]

 Thus, you get the same results.
"""


def count_matrix_paths(m, n):
    P = [0] * n
    P[0] = 1

    for i in range(m):
        for j in range(1, n):
            P[j] += P[j - 1]

    return P[n - 1]


def count_matrix_paths_recursive(m, n):
    """
    Recursive solution
    """
    def count(row, col):
        if row == m - 1 or col == n - 1:
            return 1
        return count(row + 1, col) + count(row, col + 1)

    return count(0, 0)


assert count_matrix_paths_recursive(3, 2) == 3
