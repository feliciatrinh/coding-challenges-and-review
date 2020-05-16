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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        curr = self
        while curr:
            print(curr.val, "-> ", end='')
            curr = curr.next
        print("None")


def swapPairs(head):
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
    ptr_one.next = swapPairs(ptr_swap_next)
    return new_head


linkedList = ListNode(1)
swappedLinkedList = swapPairs(linkedList)
swappedLinkedList.printNode()

linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
swappedLinkedList = swapPairs(linkedList)
swappedLinkedList.printNode()

linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
swappedLinkedList = swapPairs(linkedList)
swappedLinkedList.printNode()
