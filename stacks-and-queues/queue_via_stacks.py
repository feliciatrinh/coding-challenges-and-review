"""
Implement a MyQueue class which implements a queue using two stacks. 

Note: python's collections.deque class is a double-ended queue
(implemented as a doubly-linked list) that supports fast O(1) enqueuing and
dequeuing from either end. 
Ex)
from collections import deque
q = deque()
q.append("one")
q.append("two")
q.append("three")

q.popleft()  # returns "one"
q.popright()  # returns "three"

Can serve as either a queue or a stack.
"""


class MyQueue:
    def __init__(self):
        self.old = Stack()
        self.new = Stack()

    def add(self, item):
        self.new.push(item)

    def remove(self):
        self.fill_old()
        return self.old.pop()

    def peek(self):
        self.fill_old()
        return self.old.peek()

    def is_empty(self):
        return self.old.is_empty() & self.new.is_empty()

    def fill_old(self):
        if self.old.is_empty():
            while not self.new.is_empty():
                self.old.push(self.new.pop())


class Stack:
    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, item):
        self.array.append(item)
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.array.pop()

    def peek(self):
        return self.array[self.size - 1]

    def is_empty(self):
        return self.size == 0


Q = MyQueue()
Q.add(3)
Q.add(-1)
print(Q.peek() == 3)
Q.remove()
print(Q.remove() == -1)
Q.remove()
print(Q.is_empty())
