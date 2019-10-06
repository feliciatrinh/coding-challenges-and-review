"""
Breadth first paths using adjacency implementation of a graph G.
Assumes simple graph: no self loops
Uses a queue
time: O(V + E)
space: theta(V)
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
            

def bread_first_paths(graph, start):
    """
    Iterative solution
    Prints breadth first search graph traversal for a graph
    with integer valued vertices.
    """
    if graph is None:
        return
    marked = [False]*len(graph.adj)
    q = deque()
    q.append(start)
    marked[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for neighbor in graph.adj[v]:
            if not marked[neighbor]:
                q.append(neighbor)
                marked[neighbor] = True
                
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(5, 8)
g.add_edge(5, 2)
g.add_edge(5, 4)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 6)
g.add_edge(8, 5)

bread_first_paths(g, 0)
# should print 0, 1, 2, 4, 5, 3, 6, 8, 7
