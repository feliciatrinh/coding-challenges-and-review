# Implement a MyQueue class which implements a queue using two stacks
class MyQueue(): 
    def __init__(self): 
        self.old = Stack()
        self.new = Stack()
        
    def add(self, item): 
        self.new.push(item)
    
    def remove(self): 
        self.fillOld()
        return self.old.pop()
    
    def peek(self): 
        self.fillOld()
        return self.old.peek()
    
    def isEmpty(self): 
        return (self.old.isEmpty() & self.new.isEmpty())
        
    def fillOld(self): 
        if self.old.isEmpty(): 
            while not self.new.isEmpty(): 
                self.old.push(self.new.pop())

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
        
Q = MyQueue()
Q.add(3)
Q.add(-1)
print(Q.peek() == 3)
Q.remove()
print(Q.remove() == -1)
Q.remove()
print(Q.isEmpty())
