# Reverse a singly linked list
class Linkedlst(): 
    def __init__(self, first=None): 
        self.first = first

class Node(): 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseLinkedlst(lst): 
    if lst.first is None: 
        return 
    front = lst.first
    holder = front
    curr = front.next
    while front.next: 
        front.next = front.next.next
        curr.next = holder
        holder = curr
        curr = front.next
    lst.first = holder
    return lst

lst = Linkedlst(Node("a", Node("b", Node("c", Node("d")))))
lst = reverseLinkedlst(lst)
