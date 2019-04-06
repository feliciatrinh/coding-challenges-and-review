# Given a sorted increasing order array with unique int elements, create a BST with minimal height
# Recursive solution; runtime O(n)? for n elements? 

class TreeNode(): 
    def __init__(self, root): 
        self.root = root
        self.left = None
        self.right = None

def minimalTree(arr): 
    if len(arr) == 1: 
        return TreeNode(arr[0])
    middle = len(arr)//2
    tree = TreeNode(arr[middle])
    tree.left = makeBST(arr[0:middle])
    tree.right = makeBST(arr[middle+1:])
    return tree

makeBST([1, 2, 3, 4, 5, 6, 7])
