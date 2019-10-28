# Delete a node in the middle of a singly linked list
# input: a node from the linked lst, output: none
def deleteMiddleNode(node):
# Take over the next node
  node.val = node.next.val
  node.next = node.next.next
  return
  
