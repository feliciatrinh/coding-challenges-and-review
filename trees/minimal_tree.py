"""
Input: sorted increasing order array with unique int elements
Output: BST with minimal height

Runtime: O(n)?
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minimal_tree(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])

    middle = len(arr) // 2
    tree = TreeNode(arr[middle])
    tree.left = minimal_tree(arr[:middle])
    tree.right = minimal_tree(arr[middle + 1:])
    return tree


def list_inorder_traversal_alt(root):
    """
    Recursive solution
    Returns in-order traversal of binary tree as a list.
    """

    def inorder_traversal(root, inorder):
        if root is None:
            return
        inorder_traversal(root.left, inorder)
        inorder.append(root.value)
        inorder_traversal(root.right, inorder)
        return inorder

    return inorder_traversal(root, [])


bst = minimal_tree([1, 2, 3, 4, 5, 6, 7])
assert list_inorder_traversal_alt(bst) == [1, 2, 3, 4, 5, 6, 7]

bst = minimal_tree([-10, -3, 0, 5, 9])
