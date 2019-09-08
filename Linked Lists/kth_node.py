def kth_node(head, k):
    """
    Given the head of a linked list, return the kth to last node of the linked list
    runtime O(n)
    """
    ref = head
    main = head
    count = 0
    while count < k: 
        if ref is None: # case when k > number of nodes in linked list
            return 
        ref = ref.next
        count += 1
    # ref and main are now k nodes apart
    # when ref is None, main will point to the kth to last node 
    while ref is not None: 
        ref = ref.next
        main = main.next
    main.next = None # get rid of the rest of the linked list
    return main


def kth_node_rev(head, k):
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
