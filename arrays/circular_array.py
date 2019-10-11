"""
Input: n: number of nodes in the circular array; endNodes: list of ending nodes representing the paths taken.
Output: the node that is visited the most. If there are multiple, return the smallest numbered node.

Circular array has n nodes numbered from 1 to n.

Example:
Input: 3, [1, 3, 2, 3]
Output: 2

Paths taken: 1, 2, 3
			 3, 1, 2
			 2, 3

Nodes 2 and 3 are visited 3 times, so the lower numbered node is returned.

Input: 10, [1, 5, 10, 5]
Output: 5 (5 is visited 3 times)
"""

def circular_array_optimal(n, endNodes):

	return


def circular_array_naive(n, endNodes):
	"""
	Exceeded the runtime req.
	Iterate through the endNode array and add to visited[] accordingly.

	Attempted to optimize by keeping track of the maximum while
	adding to visited[] rather than iterating through visited[] at the end.

	Worst case: iterate through the entire array of n nodes len(endNodes) times.
	Example input: 10, [1, 10, 9, 8, 7, 6, ...]
	"""
	# 0th index remains 0 always. Use the extra space for easier indexing.
	visited = [0] * (n + 1)
	# maximum number of times a node is visited
	maximum = 0
	# the node that is visited the most
	node = 0
	for i in range(len(endNodes) - 1):
		startNode = endNodes[i]
		endNode = endNodes[i + 1]
		# simply add 1 to each of the nodes within this range.
		if startNode < endNode:
			for j in range(startNode, endNode + 1):
				visited[j] += 1 
				if visited[j] > maximum:
					maximum = visited[j]
					node = j
		elif startNode > endNode:
			for j in range(startNode, n + 1):
				visited[j] += 1
				if visited[j] > maximum:
					maximum = visited[j]
					node = j
			for k in range(1, endNode + 1):
				visited[k] += 1
				if visited[k] > maximum:
					maximum = visited[k]
					node = k
	return node
