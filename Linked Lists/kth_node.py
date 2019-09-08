def kth_node(head, k):
    """
    Given the head of a linked list, return the kth to last node of the linked list
    runtime O(n)

    Reverse the linked list first, then return the (kth - 1) node

    Can return the head of the reversed linked list if k = 1
    """ 
    if k < 1: 
        return
    rev = reverseLinkedlst(head)
    for _ in range(k - 1):
        if rev is not None: 
            rev = rev.next
    if rev is not None:
        rev.next = None # drop the rest of the linked list
    return rev

def reverseLinkedlst(head):
    """
    Iterative approach. runtime linear O(n)
    """
    prev = None
    curr = head
    while curr is not None: 
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
