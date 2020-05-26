"""
Input: sorted increasing order array with unique int elements
Output: BST with minimal height

Runtime: O(n)?
"""


class TreeNode:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


def minimal_tree(arr):
    if len(arr) == 1:
        return TreeNode(arr[0])
    middle = len(arr) // 2
    tree = TreeNode(arr[middle])
    tree.left = minimal_tree(arr[0:middle])
    tree.right = minimal_tree(arr[middle + 1:])
    return tree


minimal_tree([1, 2, 3, 4, 5, 6, 7])
