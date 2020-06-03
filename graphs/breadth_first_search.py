"""
Breadth first paths using adjacency implementation of a graph G.
Assumes simple graph: no self loops
Uses a queue.

Runtime: O(V + E)
Space complexity: O(V)
"""


def bfs(graph, start):
    """
    Returns BFS traversal of the graph as a list.
    """
    bfs_order = []
    visited = {start}
    queue = [start]
    while queue:
        v = queue.pop(0)
        bfs_order.append(v)
        for next_v in graph[v]:
            if next_v not in visited:
                queue.append(next_v)
                visited.add(next_v)
    return bfs_order


def bfs_paths(graph, start, goal):
    """
    Returns all possible paths between start and goal using BFS.
    The first path in paths will be the shortest path.
    """
    paths = []
    # queue elements are tuples of (current vertex, path from start to current vertex)
    queue = [(start, [start])]
    while queue:
        v, path = queue.pop(0)
        for next_v in graph[v]:
            if next_v == goal:
                paths.append(path + [next_v])
            else:
                if next_v not in path:
                    queue.append((next_v, path + [next_v]))
    return paths


def bfs_shortest_path(graph, start, goal):
    """
    Adapt bfs_paths_iterative() to return the shortest path between start and goal using iterative BFS.
    """
    queue = [(start, [start])]
    while queue:
        v, path = queue.pop(0)
        for next_v in graph[v]:
            if next_v == goal:
                return path + [next_v]
            else:
                if next_v not in path:
                    queue.append((next_v, path + [next_v]))
    return []


def route_between_nodes(graph, start, goal):
    """
    :return: True if there is a path between the start and goal, False otherwise
    """
    visited = {start}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for neighbor in graph[v]:
            if neighbor == goal:
                return True
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False


g = {
    0: [1, 2, 5],
    1: [],
    2: [3],
    3: [0, 7],
    4: [5, 6, 7],
    5: [1, 6],
    6: [],
    7: [6]
}

assert bfs(g, 0) == [0, 1, 2, 5, 3, 6, 7]

assert bfs_paths(g, 0, 6) == [[0, 5, 6], [0, 2, 3, 7, 6]]

assert bfs_shortest_path(g, 0, 6) == [0, 5, 6]
assert bfs_shortest_path(g, 0, 4) == []
assert bfs_shortest_path(g, 3, 6) == [3, 7, 6]
