"""
Input: Binary tree
Output: list of linked lists of all nodes at each depth of the tree
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def add(self, val):
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def __str__(self):
        curr = self
        values = ""
        while curr.next:
            values += " {} ->".format(curr.val)
            curr = curr.next
        return values + " {}".format(curr.val)


def list_of_depths(root):
    def add_to_linked_list(linked_list, val):
        if linked_list is None:
            return ListNode(val)
        linked_list.add(val)
        return linked_list

    linked_lists, queue_curr = [], []
    curr_linked_list = ListNode(tree.val)
    if tree:
        queue_curr.append(root)
    while queue_curr:
        linked_lists.append(curr_linked_list)
        queue_parents = []
        curr_linked_list = None
        # fill up queue_parents with the parent nodes
        # so that we can fill queue_curr with all the children separately
        while queue_curr:
            queue_parents.append(queue_curr.pop())
        # look at each parent node
        for parent in queue_parents:
            if parent.left:
                curr_linked_list = add_to_linked_list(curr_linked_list, parent.left.val)
                queue_curr.append(parent.left)
            if parent.right:
                curr_linked_list = add_to_linked_list(curr_linked_list, parent.right.val)
                queue_curr.append(parent.right)
    return linked_lists


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
