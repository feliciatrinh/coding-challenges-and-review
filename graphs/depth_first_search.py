"""
Depth first search can be used to find a path from start to every other
reachable vertex, visiting each vertex at most once.

Runtime: O(V + E)
Space complexity: O(V)

- mark v
- for each unmarked adjacent vertex w:
    - set edgeTo[w] = v
    - dfs(w)

- DFS preorder is order of dfs calls
- DFS postorder is order of dfs returns

Other uses for DFS:
- Finding strongly connected components.
"""


def dfs_iterative(graph, start):
    """
    Returns DFS traversal of a graph in a list.
    """
    dfs_order = []
    visited = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        dfs_order.append(v)
        for next_v in graph[v]:
            if next_v not in visited:
                stack.append(next_v)
                visited.add(next_v)
    return dfs_order


def dfs_recursive(graph, start):
    """
    Returns DFS traversal of a graph in a list.
    Recursive solution visits nodes in a different order than the iterative solution b/c it pushes nodes onto the stack
    in a different order.

    Example
    Recursive visits nodes 1, 2, then 5 but iterative visits nodes 5, 2, then 1.
    So imagine recursive solution pushes nodes onto the stack in this order: 5, 2, 1 and iterative solution pushes nodes
    onto the stack in this order: 1, 2, 5
    """
    def dfs(graph, start, visited):
        visited.add(start)
        dfs_order.append(start)

        for next_v in graph[start]:
            if next_v not in visited:
                dfs(graph, next_v, visited)

    dfs_order = []
    dfs(graph, start, set())
    return dfs_order


def dfs_recursive_print(graph, start):
    def dfs(graph, start, visited):
        visited.add(start)
        print(start, end=" ")

        for next_v in graph[start]:
            if next_v not in visited:
                dfs(graph, next_v, visited)

    dfs(graph, start, set())


def dfs_paths_recursive(graph, start, goal):
    """
    Return all possible paths between start and goal using recursive DFS.
    """
    def dfs_paths(graph, start, goal, path):
        if start == goal:
            paths.append(path)
            return

        for next_v in graph[start]:
            if next_v not in path:
                dfs_paths(graph, next_v, goal, path + [next_v])

    paths = []
    dfs_paths(graph, start, goal, [start])
    return paths


def dfs_paths_iterative(graph, start, goal):
    """
    Return all possible paths between start and goal using iterative DFS.

    Could use sets and set differences instead.
    For set s and set t,
    s.difference(t) is equivalent to s - t aka a new set with elements in s but not in t
    set.difference can take any iterable as the second arg but s - t reqs both s and t to be sets.
    """
    paths = []
    # stack elements are tuples of (current vertex, path from start to current vertex)
    stack = [(start, [start])]
    while stack:
        (v, path) = stack.pop()
        for next_v in graph[v]:
            if next_v == goal:
                paths.append(path + [next_v])
            else:
                if next_v not in path:
                    stack.append((next_v, path + [next_v]))
    return paths


def dfs_path_exists(graph, start, goal):
    """
    Recursive
    :return: True if there is a path b/w start and goal, False otherwise
    """
    def visit(graph, start, goal, visited):
        if start == goal:
            return True
        visited.add(start)
        for next_v in graph[start]:
            if next_v not in visited:
                if visit(graph, next_v, goal, visited):
                    return True

    visited = set()
    if visit(graph, start, goal, visited):
        return True
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

assert dfs_iterative(g, 0) == [0, 5, 6, 2, 3, 7, 1]
assert dfs_recursive(g, 0) == [0, 1, 2, 3, 7, 6, 5]

assert dfs_paths_iterative(g, 0, 6) == [[0, 5, 6], [0, 2, 3, 7, 6]]
assert dfs_paths_recursive(g, 0, 6) == [[0, 2, 3, 7, 6], [0, 5, 6]]

dfs_recursive_print(g, 0)
assert dfs_path_exists(g, 0, 6) is True
assert dfs_path_exists(g, 0, 4) is False
