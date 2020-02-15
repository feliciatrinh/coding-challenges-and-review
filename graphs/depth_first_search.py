"""
Depth first search can be used to find a path from start to every other
reachable vertex, visiting each vertex at most once.

- mark v
- for each unmarked adjacent vertex w: 
	- set edgeTo[w] = v
	- dfs(w)

- DFS preorder is order of dfs calls
- DFS postorder is order of dfs returns

Other uses for DFS: 
- Finding strongly connected components.
- 
"""
from collections import deque


class Graph():
    def __init__(self):
        self.adj = {}
        
    def add_edge(self, vertex, neighbor):
        """
        Adds an edge in vertex's adjacency list.
        """
        if vertex in self.adj:
            self.adj[vertex].append(neighbor)
        else:
            self.adj[vertex] = [neighbor]


def depth_first_search(graph, start):
	"""
	Assumes the graph is connected.
	recursive solution
    Prints depth first search graph traversal for a graph
    with integer valued vertices.
	"""
	visited = False * len(graph.adj)
	dfs_helper(start, visited)


def dfs_helper(v, visited):
	visited[v] = True
	print(v, end=" ")
	for w in graph.adj[v]:
		if !visited[w]:
			dfs_helper(w, visited)


def dfs_iterative(graph, start):
    """
    Iterative solution
    Prints depth first search graph traversal for a graph
    with integer valued vertices.
    Uses a stack
    """
    if graph is None:
        return
    marked = [False]*len(graph.adj)
    q = deque()
    q.append(start)
    marked[start] = True
    while q:
        v = q.pop()
        print(v, end=" ")
        for neighbor in graph.adj[v]:
            if not marked[neighbor]:
                q.append(neighbor)
                marked[neighbor] = True
	