"""
Depth first search can be used to find a path from start to every other
reachable vertex, visiting each vertex at most once.

- mark v
- for each unmarked adjacent vertex w: 
	- set edgeTo[w] = v
	- dfs(w)

- DFS preorder is order of dfs calls
- DFS postorder is order of dfs returns
"""

def depth_first_paths():
	"""
	
	"""
