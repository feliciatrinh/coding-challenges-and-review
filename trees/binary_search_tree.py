"""
- binary tree has up to two children

Basics for implementing binary search trees. 
- left subtree keys are less than the root value
- right subtree keys are greater than root value
- each left and right subtree is a BST

Operations and Runtimes: 
Search: avg O(logn), worst O(n)
Insert: avg O(logn), worst O(n)
Delete: avg O(logn), worst O(n)

Worst case occurs when you have a spindly tree.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def search(root, value):
    """
    Returns true if value is found in the BST
    """
    if root is None:
        return False
    if value < root.value:
        return search(root.left, value)
    elif value > root.value:
        return search(root.right, value)
    else:
        return True


def insert(root, value):
    """
    Insert a new node with value as its key 
    TODO: check if this is right
    """
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def delete(root, value):
    """
    Delete node with the given value as its key. 
    Must return a tree that still satisfies B tree properties. 

    Situation 1: node to be deleted is a leaf node
    - the node will be replaced with None

    Situation 2: node to be deleted has only one child
    - replace the node with its child and delete the child node

    Situation 3: node to be deleted has more than child
    - replace node with its in-order successor (smallest node in the right subtree)
      or with its in-order predecessor (greater node in the left subtree) recursively 
      until the node is a leaf of the B tree
        - in-order successor will always have null left child
    - replace the node that's now a leaf with None
    """
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        # delete the root
        if root.value == value:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            elif root.left is None and root.right is None:
                return None
            else:
                # find the smallest key in the right subtree
                # remove this smallest key from the subtree
                # set the root's value to this smallest key
                smallest = min_val(root.right)
                root.right = delete(root.right, smallest)
                root.value = smallest
    return root


def min_val(root):
    """
    Returns the smallest value in the given BST.
    Traverse through the left subtree. Average runtime is O(log(n))
    """
    if root.left:
        return min_val(root.left)
    return root.value


def is_bst(root, left=None, right=None):
    """
    Returns true if given binary tree is a BST and returns false otherwise.
    Assumes no duplicate keys. 
    Runtime O(n)
    """
    if root is None:
        return True
    # left node's value is >= root's value, not a BST
    if left is not None and left.value >= root.value:
        return False
    if right is not None and right.value <= root.value:
        return False
    return is_bst(root.left, left, root) and is_bst(root.right, root, right)


def find_height(root):
    height = 0
    if not root or (root.left is None and root.right is None):
        return height
    return 1 + max(find_height(root.left), find_height(root.right))


tree = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))
"""
        5
    3       7
  2   4   6   8

delete(tree, 5) results in 
        6
    3       7
  2  4        8  
"""
assert find_height(tree) == 2
tree = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6)))
assert find_height(tree) == 2
