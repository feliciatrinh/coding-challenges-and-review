def sortStack(stack): 
    if stack.isEmpty(): 
        return
    tempStack = Stack()
    tempStack.push(stack.pop())
    while not stack.isEmpty(): 
        val = stack.pop()
        while val > tempStack.peek(): 
            if not tempStack.isEmpty(): 
                stack.push(tempStack.pop())
        tempStack.push(val)
    return tempStack
        

class Stack(): 
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

print(sorted_stack == sortStack(stack).array)
