"""
Input: Binary tree
Output: list of linked lists of all nodes at each depth of the tree
"""


class TreeNode():
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self, first=None):
        self.first = first

    def add(self, item):
        if self.first:
            tail = self.first
            while tail.next:
                tail = tail.next
            tail.next = item
        else:
            self.first = item

    def __str__(self):
        curr = self.first
        values = ""
        while curr.next:
            values += " {} ->".format(curr.val)
            curr = curr.next
        return values + " {}".format(curr.val)


class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def list_of_depths(tree):
    lst, queue_curr = [], []
    curr_level = LinkedList(Node(tree.root))
    if tree:
        queue_curr.append(tree)
    while queue_curr:
        lst.append(curr_level)
        queue_parents = []
        curr_level = LinkedList()  # the linked list for this depth
        # fill up queue_parents with the parent nodes 
        # so that we can fill queue_curr with all the children separately
        while queue_curr:
            queue_parents.append(queue_curr.pop())
        # look at each parent node
        for parent in queue_parents:
            if parent.left:
                # add this node to this depth's linked list
                curr_level.add(Node(parent.left.root))
                queue_curr.append(parent.left)
            if parent.right:
                curr_level.add(Node(parent.right.root))
                queue_curr.append(parent.right)
    return lst


# tests for visualization purposes
tree = TreeNode(1)
lst = list_of_depths(tree)
for level in lst:
    print(level)

tree = TreeNode(1, left=TreeNode(2))
lst = list_of_depths(tree)
for level in lst:
    print(level)

tree = TreeNode(1, left=TreeNode(2), right=TreeNode(2))
lst = list_of_depths(tree)
for level in lst:
    print(level)

tree.left.left, tree.left.right = TreeNode(3), TreeNode(3)
tree.right.left, tree.right.right = TreeNode(3), TreeNode(3)
lst2 = list_of_depths(tree)
for level in lst2:
    print(level)
