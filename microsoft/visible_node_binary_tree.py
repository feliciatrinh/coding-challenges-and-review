"""
Input: binary tree
Output: count the number of visible nodes in the binary tree

In a binary tree, if there is no node with greater value than A's in the path from root to node A, then node A is
visible.

Input:  5
    3       10
 20  21   1
Output: 4
Visible nodes are 5, 20, 21, 10

Input: -10
          -15
             -1
Output: 2
Visible nodes are -10, -1

Idea
- the root is always a visible node
- dsf?
- keep track of the max value seen so far as you traverse from the root down to the leaves
    - max_value is initially the root value, so root is visible
    - recursively run alg in left and right branch: at node 3, the max_value is 5 so node 3 is not visible
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def visible_nodes(root):
    """
    Runtime: O(n), Space complexity: O(n) for recursion stack?
    """
    def count_visible(node, max_value):
        count = 0
        if node is not None:
            if node.val >= max_value:
                max_value = node.val
                count = 1
            return count_visible(node.left, max_value) + count_visible(node.right, max_value) + count
        return count

    return count_visible(root, root.val)


tree = TreeNode(5, left=TreeNode(3, left=TreeNode(20), right=TreeNode(21)), right=TreeNode(10, left=TreeNode(1)))
assert visible_nodes(tree) == 4

tree = TreeNode(-10, right=TreeNode(-15, right=TreeNode(-1)))
assert visible_nodes(tree) == 2
