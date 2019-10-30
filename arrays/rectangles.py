"""
Input: 2D array of 1's and 0's
Output: list of all starting and ending points of rectangles filled with 0's

Rectangle can be a single 0.
Assume rectangles cannot touch each other. 

Example output: [[(2, 3), (3, 5)], [(3, 6), (5, 6)]]
"""

def rectangles(matrix):
	"""
	As we iterate through the matrix, once we find a starting 0
	we look to the right and down for the ending 0. 
	Replace these 0's by 1 so that we don't double count
	these as rectangles as we traverse through the rest of the matrix.
	Can optimize by making the outer loop the smaller dimension.
	"""
	result = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				# note the starting position
				position = []
				position.append((i, j))
				last_row, last_col = helper(matrix, i, j)
				position.append((last_row, last_col))
				result.append(position)
	return result


def helper(matrix, i, j):
	"""
	Returns the row, col of the last 0 in the rectangle.
	"""
	last_row = i
	last_col = j
	for row in range(i, len(matrix)):
		for col in range(j, len(matrix[0])):
			if matrix[row][col] == 0:
				matrix[row][col] = 1
				last_col = col
				last_row = row
			else:
				if row > last_row or row == len(matrix):
					return last_row, last_col
				break
	return last_row, last_col


matrix = [
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0]
]

print(rectangles(matrix))
