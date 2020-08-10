"""
Source: Leetcode
Input: binary tree, two nodes in the tree
Output: lowest common ancestor (LCA) of the given two nodes in the tree

All node values are unique.
The two given nodes are different and both exist in the tree.

Runtime: O(n), Space complexity: O(n)

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example
        3
   5         1
6    2    0    8
   7  4

Input: tree, 5, 1
Output: 3

Input: tree, 5, 4
Output: 5

Ideas
- can use BFS to get the path between two nodes or detect if a path exists b/w two nodes?

- start at node1, traverse its children
    - if you find node2 in node1's children then node 1 is the LCA
    - vice verse for node2

- start at node1, go up to the parent, traverse down the other branch
    - if you find node2, then node1's parent is the LCA
    - if you reach leaves and don't find node2, then go up to the grand parent and traverse the other branch in the
      same way
    - can i optimize this idea by first determining which node is higher up in the tree
        - then i would only have to go up starting from the higher node
        - can keep track of the depth in the parents dictionary as well
    - to be able to go up, i'd have to keep track of the parents as i traverse down the tree
        - can add a parent attribute to TreeNode or keep a dictionary of node, parent

    def set_parents_attribute(node, parent):
        if node is None:
            return
        node.parent = parent
        set_parents_attribute(node.left, node)
        set_parents_attribute(node.right, node)
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Runtime: O(n), Space complexity: O(n)
    """
    def set_parents_dict(node, parent, depth):
        """
        Stores the parent and depth of each node in a dictionary.
        Can stop early when p and q have been found.
        """
        if node is None or (p in parents and q in parents):
            return
        parents[node.val] = (parent, depth)
        set_parents_dict(node.left, node, depth + 1)
        set_parents_dict(node.right, node, depth + 1)

    def in_children(node, goal):
        """
        :return: True if goal is one of node's children, False otherwise
        """
        if node is not None:
            if node.left == goal or node.right == goal:
                return True
            return in_children(node.left, goal) or in_children(node.right, goal)
        return False

    def traverse_up_and_search(start, goal):
        """
        Starting from start, traverse up to the parent and search the branch that doesn't contain the start node for the
        goal node.
        Return parent node when goal node is found.
        """
        parent = parents[start.val][0]
        if parent.left == start:
            if parent.right == goal or in_children(parent.right, goal):
                return parent
        elif parent.right == start:
            if parent.left == goal or in_children(parent.left, goal):
                return parent
        return traverse_up_and_search(parent, goal)

    parents = {}
    set_parents_dict(root, None, 0)

    # determine node with lower depth if any to avoid searching the other branch unnecessarily
    depth_p = parents[p.val][1]
    depth_q = parents[q.val][1]
    if depth_p < depth_q:
        if in_children(p, q):
            return p
        return traverse_up_and_search(p, q)
    else:
        if in_children(q, p):
            return q
    return traverse_up_and_search(q, p)


n0 = TreeNode(0)
n8 = TreeNode(8)
n6 = TreeNode(6)
n7 = TreeNode(7)
n4 = TreeNode(4)
n2 = TreeNode(2, left=n7, right=n4)
n5 = TreeNode(5, left=n6, right=n2)
n1 = TreeNode(1, left=n0, right=n8)
root = TreeNode(3, left=n5, right=n1)

assert lowest_common_ancestor(root, n5, n4) == n5
assert lowest_common_ancestor(root, n5, n1) == root
