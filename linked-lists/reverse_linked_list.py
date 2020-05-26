"""
Input: head of a singly linked list
Output: the reverse linked list

Reverse a singly linked list

Runtime: O(n)
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


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


def reverse_linked_list_recursive(head):
    """
    Recursive approach. runtime O(n)
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    # make the next node point to the current node
    head.next.next = head
    # the current head becomes the last node
    head.next = None
    return new_head


lst = Node("a", Node("b", Node("c", Node("d"))))
reverse = reverse_linked_list(lst)
original = reverse_linked_list(reverse)
assert lst == original

reverse = reverse_linked_list_recursive(lst)
original = reverse_linked_list_recursive(reverse)
assert lst == original
