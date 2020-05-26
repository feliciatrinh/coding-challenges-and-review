"""
Input: head of a singly-linked list
Output: True if linked list contains a cycle and False otherwise

Runtime: O(n)
Space complexity: O(1)

Two Pointer Method
- Keep a pointer that moves to the next node, one node at a time.
- Keep a second pointer that moves two nodes at a time.
- Pointer 1 and pointer 2 start at different nodes, so the only way they can
  end up at the same node is if there's a cycle in the linked list.
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def detect_cycle(head: Node) -> bool:
    if not head:
        return False
    jump_one_ptr = head
    jump_two_ptr = head.next
    while jump_one_ptr is not None and jump_two_ptr is not None:
        if jump_two_ptr == jump_one_ptr:
            return True
        jump_one_ptr = jump_one_ptr.next
        jump_two_ptr = jump_two_ptr.next
        if jump_two_ptr is not None:
            jump_two_ptr = jump_two_ptr.next
    return False
