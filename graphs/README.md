# Graphs

* [Breadth First Search](breadth_first_paths.py)
	* Use breadth first search graph traversal algorithm to print the breadth first path.
	* Uses adjacency list implementation for graph G.
	* Uses a queue to keep track of vertices.
	* Runtime O(V + E), Space O(V)
* [Depth First Search](depth_first_search.py)
	* Find a path from start to every other reachable vertex, visiting each vertex only once.
	* Uses adjacency list implementation for graph G.
	* Uses a stack.
	* Runtime O(V + E), Space O(V)
* [Longest Increasing Subsequence LIS](longest_increasing_subsequence.py)
	* Given an array of integers, return the longest increasing subsequence.
	* Dynamic programming: turns the problem into a DAG. Runtime O(n^2)
