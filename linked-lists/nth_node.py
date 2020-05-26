"""
Source: leetcode
Input: head to linked list
Output: head of the linked list after removing the n-th node

Given a linked list, remove the n-th node from the end of list and return its head.

Runtime: O(n)

Two pointer method
- Advance the first ptr by n nodes
- Then, advance the first ptr and second ptr until the first ptr is None.
- Now, the two pointers will be n nodes apart.
- So the first ptr will be at the nth node from the end
- Keep a reference to the previous node so you can delete the nth node
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def nth_node(head, n):
    """
    Source: leetcode
    Basing it off of my old solution.
    Assume n is always valid.
    """
    first = head
    second = head
    while n > 0:
        first = first.next
        n -= 1

    # first is already None, so we remove the first node
    if not first:
        return head.next

    while first is not None:
        prev = second
        first = first.next
        second = second.next

    prev.next = second.next
    return head


#########################################################################
###### PAST SOLUTIONS AND SLIGHT PROBLEM VARIATIONS ARE FOUND BELOW #####
#########################################################################


def kth_node(head, k):
    """
    Given the head of a linked list, return the kth to last node of the linked list
    using two pointer method. 
    runtime O(n)
    """
    ref = head
    main = head
    count = 0
    while count < k:
        if ref is None:  # case when k > number of nodes in linked list
            return
        ref = ref.next
        count += 1
    # ref and main are now k nodes apart
    # when ref is None, main will point to the kth to last node 
    while ref is not None:
        ref = ref.next
        main = main.next
    main.next = None  # get rid of the rest of the linked list
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
    rev = reverse_linked_list(head)
    for _ in range(k - 1):
        if rev is not None:
            rev = rev.next
    if rev is not None:
        rev.next = None  # drop the rest of the linked list
    return rev


def reverse_linked_list(head):
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
