# Given a binary tree, design an algorithm which creates a linked list of all nodes at each depth

# function to visualize each linked list containing nodes at a single depth
def printLinkedlst(lst): 
    if not lst.first: 
        return
    tail = lst.first
    vals = []
    while tail: 
        vals.append(tail.val)
        tail = tail.next
    print(*vals)

# returns a list of linked list containing all nodes at each depth
def listofDepths(tree): 
    lst, queue_curr = [], []
    curr_level = Linkedlst(Node(tree.root))
    if tree: 
        queue_curr.append(tree) 
    while queue_curr: 
        lst.append(curr_level)
        queue_parents = []
        curr_level = Linkedlst() # the linked list for this depth
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
    
class Linkedlst(): 
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

class Node(): 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode(): 
    def __init__(self, root, left=None, right=None): 
        self.root = root
        self.left = left
        self.right = right

# tests for visualization purposes
tree = TreeNode(1, TreeNode(2), TreeNode(2))
lst = listofDepths(tree)
for level in lst: 
    printLinkedlst(level)

tree.left.left, tree.left.right = TreeNode(3), TreeNode(3)
tree.right.left, tree.right.right = TreeNode(3), TreeNode(3)
lst2 = listofDepths(tree)
for level in lst2: 
    printLinkedlst(level)
