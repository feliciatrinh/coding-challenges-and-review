// Reverse a linked list in java iteratively
public static Node reverse(Node head) {
  Node prev = null; 
  Node curr = head; 
  Node next; 
  
  while (curr != null) {
    next = curr.next; 
    curr.next = prev; 
    prev = curr; 
    curr = next; 
  }
  return prev; 
}
