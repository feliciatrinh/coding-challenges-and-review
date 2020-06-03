"""
Source: UC Berkeley CS61B
Design your implementation of a doubly linked list.

Operations
get: should return the element at specified index i
size: should return the number of elements in the doubly linked list.
insert_front: should insert the new element at the front of the list
insert_back: should insert the new element at the end of the list
delete_front: should delete the element at the front of the list and return the value
delete_back: should delete the element at the back of the list and return the value
to_string: should return string representation of the IntDList in the form [] for empty list or [1, 2] for list with elements etc.

insert_at_index: should insert the new element at the specified index (including front and back).
After insertion, the element should be at index i and the successive elements (if any) would have been shifted right by 1 index position.

delete_at_index: should delete the element at the specified index (including front and back) and return the value.
After deletion, the successive elements (if any) would have been shifted left by 1 index position.
"""


class DNode:
    def __init__(self, prev_node=None, val=0, next_node=None):
        self.prev = prev_node
        self.val = val
        self.next = next_node


class DoubleLinkedList:
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def get(self, index):
        """
        :returns the element at specified index i
        """
        curr_node = self.front
        while index > 0:
            curr_node = curr_node.next
        return curr_node

    def size(self):
        """
        :returns the number of elements
        """
        pass

    def insert_front(self):
        """
        inserts the new element at the front of the list
        """
        pass

    def insert_back(self):
        """
        inserts the new element at the back of the list
        """
        pass

    def delete_front(self):
        """
        deletes the element at the front of the list and returns the value
        """
        pass

    def delete_back(self):
        """
        deletes the element at the back of the list and returns the value
        """
        pass

    def insert_at_index(self, index):
        """
        inserts the element at specified index i
        """
        pass

    def delete_at_index(self, index):
        """
        deletes the element at specified index i and returns the value
        """
        pass

    def __str__(self):
        pass
