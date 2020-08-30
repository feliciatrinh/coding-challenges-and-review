"""
Returns true if given binary tree is a BST and returns false otherwise.
Assumes no duplicate keys.

Runtime O(n)

Example
        5
   3         9
1    4    7    10
        6   8
Output: True

        3
   5         1
6    2    0    8
   7  4
Output: False

- Each node has only one parent and that parent is either to the right or to the left of the node
- If the parent is to the right, the node needs to be less than it
- If the parent is to the left, the node needs to be greater than it
"""


def is_bst(root, left=None, right=None):
    if root is None:
        return True
    # left node's value is >= root's value, not a BST
    if left is not None and left.value >= root.value:
        return False
    if right is not None and right.value <= root.value:
        return False
    return is_bst(root.left, left, root) and is_bst(root.right, root, right)
