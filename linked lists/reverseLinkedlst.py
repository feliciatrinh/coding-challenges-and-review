"""
Input: head of a singly linked list
Output: the reverse linked list

Reverse a singly linked list

Runtime: O(n)
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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


def reverseLinkedListRecursive(head):
    """
    Recursive approach. runtime O(n)
    """
    if head is None or head.next is None: 
        return head
    new_head = reverseLinkedListRecursive(head.next)
    # make the next node point to the current node
    head.next.next = head
    # the current head becomes the last node
    head.next = None
    return new_head


lst = ListNode("a")
lst.next = ListNode("b")
lst.next.next = ListNode("c")
lst.next.next.next = ListNode("d")
reverse = reverseLinkedlst(lst)
original = reverseLinkedlst(reverse)
assert lst == original

reverse = reverseLinkedListRecursive(lst)
original = reverseLinkedListRecursive(reverse)
assert lst == original
