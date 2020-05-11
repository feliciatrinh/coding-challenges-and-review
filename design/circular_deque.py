"""
Source: leetcode
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
"""


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.frontIndex = 0
        self.lastIndex = 1
        self.deque = [0] * self.capacity
        self.size = 0  # current size
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size != self.capacity:
            self.deque[self.frontIndex] = value
            self.size += 1
            if self.frontIndex == 0:
                self.frontIndex = self.capacity - 1
            else:
                self.frontIndex -= 1                
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size != self.capacity:
            self.deque[self.lastIndex] = value
            self.size += 1
            if self.lastIndex == self.capacity - 1:
                self.lastIndex = 0
            else:
                self.lastIndex += 1
            return True
        return False
        
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        if self.frontIndex == self.capacity - 1:
            self.frontIndex = 0
        else:
            self.frontIndex += 1
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False

        if self.lastIndex == 0:
            self.lastIndex = self.capacity - 1
        else:
            self.lastIndex -= 1
        self.size -= 1
        return True        

    
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size == 0:
            return -1
        if self.frontIndex == self.capacity - 1:
            return self.deque[0]
        return self.deque[self.frontIndex + 1]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size == 0:
            return -1
        if self.lastIndex == 0:
            return self.deque[self.capacity - 1]
        return self.deque[self.lastIndex - 1]        

    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
