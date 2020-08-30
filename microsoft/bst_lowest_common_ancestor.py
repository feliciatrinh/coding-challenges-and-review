"""
Input: binary search tree, two nodes in the tree
Output: lowest common ancestor (LCA) of the given two nodes in the tree

Runtime: O(logn) on average, worst case O(n) if spindly tree
Space complexity: O(n) for recursion stack

Lowest Common Ancestor: The lowest common ancestor is defined between two nodes node1 and node2 as the lowest node in T
that has both node1 and node2 as descendants (where we allow a node to be a descendant of itself).

All of the nodes’ values will be unique.
node1 and node2 are different and both values will exist in the BST.
Assume BST is not spindly (non-pathological), so you won't run into a worst-case runtime of O(n)

You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.

Example
        5
   3         9
1    4    7    10
        6   8

Input: tree, 6, 10
Output: 9

Input: tree, 3, 9
Output: 5

Input: tree, 3, 4
Output: 3

Ideas:
- if p and q are on different sides of the root, then you know the root is the LCA
    - you can apply this logic as you go down the right or left side of the tree depending on the values of p and q
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Recursive approach
    Average runtime: O(logn), Worst case runtime: O(n), Space complexity: O(n)
    """
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root


def lowest_common_ancestor_iter(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Iterative approach
    Average runtime: O(logn), Worst case runtime: O(n), Space complexity: O(1)
    """
    ancestor = root
    while ancestor is not None:
        if p.val < ancestor.val and q.val < ancestor.val:
            ancestor = ancestor.left
        elif p.val > ancestor.val and q.val > ancestor.val:
            ancestor = ancestor.right
        else:
            return ancestor


n6 = TreeNode(6)
n8 = TreeNode(8)
n7 = TreeNode(7, left=n6, right=n8)
n10 = TreeNode(10)
n9 = TreeNode(9, left=n7, right=n10)
n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3, left=n1, right=n4)
n5 = TreeNode(5, left=n3, right=n9)

assert lowest_common_ancestor(n5, n6, n10) == n9
assert lowest_common_ancestor(n5, n3, n4) == n3
assert lowest_common_ancestor(n5, n4, n8) == n5

assert lowest_common_ancestor_iter(n5, n6, n10) == n9
assert lowest_common_ancestor_iter(n5, n3, n4) == n3
assert lowest_common_ancestor_iter(n5, n4, n8) == n5
