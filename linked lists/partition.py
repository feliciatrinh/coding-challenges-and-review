# Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
def partition(lst, x): 
    curr = lst.first
    lessFront, lessLast = None, None
    greaterFront, greaterLast = None, None

    while curr: 
        if curr.val < x:
            if lessFront: 
                lessLast.next = curr
                lessLast = lessLast.next
            else: 
                lessFront = curr
                lessLast = curr
        else: 
            if greaterFront: 
                greaterLast.next = curr
                greaterLast = greaterLast.next
            else: 
                greaterFront = curr
                greaterLast = curr
        curr = curr.next
    if lessFront: 
        lessLast.next = greaterFront
        return lessFront
    return greaterFront
    
class Linkedlst(): 
    def __init__(self, first=None): 
        self.first = first
        
class Node(): 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
