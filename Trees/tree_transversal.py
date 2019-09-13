"""
- Pre-order traversal is SHOUT LEFT
    - parent first, then left, then right
- In-order traversal is SHOUT BELOW
    - left first, then parent, then right
- Post-order traversal is SHOUT RIGHT
    - left first, then right, then parent

- In-order: 
    - produces sorted output
    - can produce in-order by sorting any of the other traversals

- Can reconstruct the B tree given pre-order, post-order, or level-order
"""

class Node():
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None


def list_levelorder_traversal(root):
    """
    Iterative
    Returns level-order traversal of B tree as a list.

        3
       / \
      9  20
        /  \
       15   7 

    returns [3, 9, 20, 15, 7]

    Note: python's collections.deque class is a double-ended queue
    (implemented as a doubly-linked list) that supports fast O(1) enqueuing and
    dequeuing from either end. Can be used as a queue or a stack.
    We will use it as a queue here.

    Start from the root. temp_node = root
    Loop while node is not null
        - add temp_node.value to list
        - enqueue temp_node's left then right children to q
        - dequeue a node from q and assign it's value to temp_node
    """
    from collections import deque
    q = deque()
    lst = []
    if root: 
        q.append(root)
    while q:
        temp_node = q.popleft()
        lst.append(temp_node.value)
        if temp_node.left:
            q.append(temp_node.left)
        if temp_node.right:
            q.append(temp_node.right)
    return lst


def list_levelorder(root):
    """
    Iterative
    Returns level-order traversal of B tree as a list of lists

        3
       / \
      9  20
        /  \
       15   7 

    returns [[3], [9, 20], [15, 7]]
    """
    lst = []
    curr_level = []
    if root: 
        curr_level.append(root)
    while curr_level:
        values = []
        next_level = []
        for node in curr_level:
            values.append(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        lst.append(values)
        curr_level = next_level
    return lst


def print_level_order(root):
    """
    Prints level order traversal. Each level on a separate line.
    ex) 3

        9 20

        15 7
    TODO: figure out a way to do so i
    """
    curr_level = []
    if root: 
        curr_level.append(root)
    while curr_level:
        values = []
        next_level = []
        for i in range(len(curr_level)):
            node = curr_level[i]
            values.append(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if i < len(curr_level) - 1:
                # print(values[i]),  # syntax for python2, prints on same line
                print(values[i], end=" ")
            else:
                print(values[i])
        curr_level = next_level

def print_preorder_traversal(root):
    """
    Recursive solution
    Prints the pre-order traversal of binary tree.
    """
    if root:
        print(root.value)
        print_preorder_traversal(root.left)
        print_preorder_traversal(root.right)


def list_preorder_traversal(root):
    """
    Recursive solution
    Returns pre-order traversal of B tree as a list.
    """
    preorder = []
    if root:
        preorder.append(root.value)
        for val in list_preorder_traversal(root.left):
            preorder.append(val)
        for val in list_preorder_traversal(root.right):
            preorder.append(val)
    return preorder


def print_inorder_traversal(root):
    """
    Recursive solution
    Prints the in-order traversal of binary tree.
    """
    if root:
        print_inorder_traversal(root.left)
        print(root.value)
        print_inorder_traversal(root.right)


def list_inorder_traversal(root):
    """
    Recursive solution
    Returns in-order traversal of B tree as a list.
    """
    inorder = []
    if root:
        for val in list_inorder_traversal(root.left):
            inorder.append(val)
        inorder.append(root.value)
        for val in list_inorder_traversal(root.right):
            inorder.append(val)
    return inorder


def print_postorder(root):
    """
    Recursive solution
    Prints the post-order traversal of binary tree.
    """
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.value)


def list_postorder_traversal(root):
    """
    Recursive solution
    Returns post-order traversal of B tree as a list.
    """
    postorder = []
    if root:
        for val in list_postorder_traversal(root.left):
            postorder.append(val)
        for val in list_postorder_traversal(root.right):
            postorder.append(val)
        postorder.append(root.value)
    return postorder
