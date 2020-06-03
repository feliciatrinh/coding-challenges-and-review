"""
Source: Leetcode
Input: binary tree
Output: True if tree is symmetric, False otherwise

Runtime: O(n)
Space: O(n)

Idea 1 BAD
- Find the in-order traversal of the tree and check if it's a palindrome
- Won't work on a tree like TreeNode(1, left=TreeNode(2, left=TreeNode(2)), right=TreeNode(2, left=TreeNode(2)))
  because in-order traversal can't account for those null leaves

Idea 2 from Leetcode
- make a copy of the tree
- see if the two trees are mirror reflections of each other because a tree is symmetric when its two subtrees are mirror
  reflections of each other
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def is_mirror(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val == node2.val:
            return is_mirror(node1.right, node2.left) and is_mirror(node1.left, node2.right)
        return False

    return is_mirror(root, root)


tree = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
assert is_symmetric(tree) is True

tree = TreeNode(1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3)))
assert is_symmetric(tree) is False

tree = TreeNode(1, left=TreeNode(2, left=TreeNode(2)), right=TreeNode(2, left=TreeNode(2)))
assert is_symmetric(tree) is False
