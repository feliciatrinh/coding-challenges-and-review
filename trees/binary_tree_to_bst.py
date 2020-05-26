"""
Source: Leetcode
Input: Binary tree
Output: Binary Search Tree with the same spatial structure

Runtime: O(nlogn) for sorting
Space compexity: O(n)

Can achieve O(1) space complexity by using Morris Traversal.

Example
Input:
          0
    1           2
 3     4      5
  6             7
   8
Binary seach tree:
          5
    3           8
 0     4      6
  1             7
   2

Idea
- Traverse the binary tree using in-order, pre-order, post-order, etc.
- Sort the traversal array
- Traverse the binary tree using in-order traversal and replace the value of the current node with the sorted array's
  current value.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root, inorder):
    """
    Recursive solution
    Returns in-order traversal of binary tree as a list.
    """
    if root is None:
        return

    inorder_traversal(root.left, inorder)
    inorder.append(root.val)
    inorder_traversal(root.right, inorder)
    return inorder


def binary_tree_to_bst(root: Node) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def change_node_vals(root, sorted_inorder):
        """
        Traverses through the binary tree using in-order traversal and replaces the current node value with
        sorted_inorder[index].
        """
        if root is None:
            return

        change_node_vals(root.left, sorted_inorder)

        root.val = sorted_inorder[0]
        sorted_inorder.pop(0)

        change_node_vals(root.right, sorted_inorder)

    inorder = inorder_traversal(root, [])
    inorder.sort()
    change_node_vals(root, inorder)


bt1 = Node(0, left=Node(1, left=Node(3, right=Node(6, right=Node(8))), right=Node(4)),
           right=Node(2, left=Node(5, right=Node(7))))
binary_tree_to_bst(bt1)
assert inorder_traversal(bt1, []) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
