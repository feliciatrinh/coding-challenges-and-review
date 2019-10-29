"""
Print all possible paths from the top left to the bottom right of an m x n matrix.

Input: m x n matrix
Output: Paths as lists

Solution: use recursion to determine all possible paths when you can only move down and to the right.
Runtime: exponential

Solution: Could solve using dynamic programming instead to get a better runtime.

Example: 
[[1, 2, 3], 
 [4, 5, 6],
 [7, 8, 9]]

Has paths
[1, 4, 7, 8, 9]
[1, 4, 5, 8, 9]
[1, 4, 5, 6, 9]
[1, 2, 5, 8, 9]
[1, 2, 5, 6, 9]
[1, 2, 3, 6, 9]
"""


def matrix_paths(matrix):
	return matrix_paths_helper(matrix, 0, 0, [0]*(len(matrix) + len(matrix[0]) - 1), 0)
	

def matrix_paths_helper(matrix, row, col, path, index):
	"""
	We need an index because we want to re-write the path array during each of the possible paths.
	Appending the element to the path doesn't work because you have no way of starting a new path
	and the path array just keeps getting longer.
	"""
	num_col = len(matrix[0])
	num_row = len(matrix)
	# When you are in the last column, you can only go down.
	if col == num_col - 1:
		for j in range(row, num_row): 
			path[index] = (matrix[j][col])
			index += 1
		print(path)
		return
	# When you are in the last row, you can only go right.
	if row == num_row - 1:
		for i in range(col, num_col):
			path[index] = (matrix[row][i])
			index += 1
		print(path)
		return
	# Step to the right or step down and recurse.
	path[index] = (matrix[row][col])
	matrix_paths_helper(matrix, row + 1, col, path, index + 1)
	matrix_paths_helper(matrix, row, col + 1, path, index + 1)


def count_matrix_paths_recursive(matrix, row, col):
	"""
	Returns the number of paths you can take to go from top left to bottom right of matrix.
	"""
	# If you are in the last row or column, you only have one path possible.
	num_col = len(matrix[0])
	num_row = len(matrix)
	if row == num_row - 1 or col == num_col - 1:
		return 1
	return count_matrix_paths_recursive(matrix, row + 1, col) + count_matrix_paths_recursive(matrix, row, col + 1)
