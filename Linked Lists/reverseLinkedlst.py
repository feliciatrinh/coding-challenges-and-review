# Reverse a singly linked list
class Linkedlst():
    def __init__(self, head=None): 
        self.head = head

class Node():
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

def reverseLinkedlst(lst):
    """
    Iterative approach. runtime linear O(n)
    """
    prev = None
    curr = lst.head
    while curr is not None: 
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

#lst = Linkedlst(Node("a", Node("b", Node("c", Node("d")))))9

def reverseLinkedListRecursive(head):
    """
    Recursive approach. runtime O(n)
    """
    if head is None or head.next is None: 
        return head
    new_head = reverseLinkedlst(head.next)
    # make the next node point to the current node
    head.next.next = head
    # the current head becomes the last node
    head.next = None
    return new_head
