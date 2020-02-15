"""
A* algorithm used to find the least-cost path to a goal node in graph G.
Is an informed search algorithm; meant to reduce the number of nodes
you expand unnecessarily.

Assumes simple graph: no self loops
Uses a priority queue
time: depends on heuristic, worst case of unbounded search space is O(|E|) = O(b^d)
for branch factor b and solution depth d
space: O(|V|) = O(b^d)
"""
