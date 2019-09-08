# Reverse a singly linked list
class Linkedlst():
    def __init__(self, head=None): 
        self.head = head

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseLinkedlst(lst):
    """
    Iterative approach. runtime linear O(n)
    """
    prev = None
    curr = lst.head
    while curr is not None: 
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

#lst = Linkedlst(Node("a", Node("b", Node("c", Node("d")))))

def reverseLinkedListRecursive(lst):
    """
    Recursive approach. runtime O(n)
    """
    if lst is None or lst.next is None: 
        return lst
    new_head = reverseLinkedlst(lst.next)
    # make the next node point to the current node
    lst.head.next.next = lst.head
    # the current head becomes the last node
    lst.next = None
    return new_head
