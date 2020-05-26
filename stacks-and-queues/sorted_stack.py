"""
Sort a stack s.t. the smallest items are on the top. Can use an additional temporary stack.
"""


def sort_stack(stack):
    if stack.is_empty():
        return
    temp_stack = Stack()
    temp_stack.push(stack.pop())
    while not stack.is_empty():
        val = stack.pop()
        while val > temp_stack.peek():
            if not temp_stack.isEmpty():
                stack.push(temp_stack.pop())
        temp_stack.push(val)
    return temp_stack


class Stack:
    def __init__(self):
        self.array = []
        self.length = 0

    def push(self, item):
        self.array.append(item)
        self.length += 1

    def pop(self):
        if not self.isEmpty():
            self.length -= 1
            return self.array.pop()

    def peek(self):
        return self.array[self.length - 1]

    def isEmpty(self):
        return self.length == 0


stack = Stack()
stack.push(0)
stack.push(4)
stack.push(2)
stack.push(1)
stack.push(5)
sorted_stack = [5, 4, 2, 1, 0]

print(sorted_stack == sort_stack(stack).array)
