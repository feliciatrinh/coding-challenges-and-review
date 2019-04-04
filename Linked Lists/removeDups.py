# Remove duplicates from a singly linked list
def removeDups (lst): 
    current = lst.first
    if current is None: 
        return
    values = set((current.val))
    while current.next: 
        if current.next.val in values:
            current.next = current.next.next
        current = current.next
        values.add(current.val)
    return
