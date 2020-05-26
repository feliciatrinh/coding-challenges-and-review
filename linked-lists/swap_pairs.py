"""
Input: linked list
Output: head of the linked list with every two nodes swapped

Given a linked list, swap every two adjacent nodes and return its head.

Runtime: O(n)

Example
Given 1->2->3->4, you should return the list as 2->1->4->3.

- Use three ptrs to keep track
- Swap the first two nodes, keep a ref to the new head
- Recursively swap the rest of the linked list
"""


class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        curr = self
        values = ""
        while curr.next:
            values += " {} ->".format(curr.val)
            curr = curr.next
        return values + " {}".format(curr.val)


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    ptr_one = head
    ptr_two = head.next
    # ptr to the rest of the linked list that you still need to swap
    ptr_swap_next = ptr_two.next
    # swap the second and first nodes
    ptr_two.next = ptr_one
    # ptr to the new head of the resultant linked list
    new_head = ptr_two
    ptr_one.next = swap_pairs(ptr_swap_next)
    return new_head


linked_lists = [
    Node(1),
    Node(1, Node(2, Node(3, Node(4)))),
    Node(1, Node(2, Node(3, Node(4, Node(5))))),
]

for lst in linked_lists:
    print(swap_pairs(lst))
