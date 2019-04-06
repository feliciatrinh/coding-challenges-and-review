# Adapted iterative BFS to find if there is a route between two nodes
# rather than using a list for the queue and popping off the 0 index item, could use an actual queue

def routeBetweenNodes(graph, start, end): 
    visited = []
    queue = []
    queue.append(start)
    visited.append(start)
    while queue: 
        vert = queue.pop(0)
        # Look at each neighbor of vert
        for neighbor in graph[vert]: 
            if neighbor not in visited: 
                if neighbor == end: 
                    return True
                # add neighbor to the queue to ensure that you visit its neighbors too
                queue.append(neighbor)
                visited.append(neighbor)
    return False
