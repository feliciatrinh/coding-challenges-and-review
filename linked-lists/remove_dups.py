"""
Input: singly linked list
Output: singly linked list without duplicate values

Runtime: O(n)
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        curr = self
        values = ""
        while curr.next:
            values += " {} ->".format(curr.val)
            curr = curr.next
        return values + " {}".format(curr.val)


def remove_dups(head):
    if head is None:
        return

    prev = head
    curr = head.next
    values = {prev.val}
    while curr:
        if curr.val in values:
            prev.next = curr.next
        else:
            values.add(curr.val)
            prev = curr
        curr = curr.next
    return head


head = Node(0, Node(1, Node(2, Node(1, Node(3, Node(2, Node(2)))))))
print(remove_dups(head))
