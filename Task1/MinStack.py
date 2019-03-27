class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        return list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        top = self.pop()
        if (top == self.min) 
            self.min = self[len(self)-1]
        self.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self[len(self)-1]

    def getMin(self):
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()