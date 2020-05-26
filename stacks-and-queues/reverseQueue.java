// Reverse a stack using a queue in java
Stack<Integer> stack = new Stack<Integer>();
Queue<Integer> queue = new ArrayDeque<Integer>();
  stack.push(1);
  stack.push(2);
  stack.push(3);
  while (!stack.isEmpty()) {
      queue.add(stack.pop());
  }
  while (!queue.isEmpty()) {
      stack.push(queue.remove());
  }
