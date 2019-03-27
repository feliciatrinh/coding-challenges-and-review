class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        A double linked list
        """
        self.first = None
        self.last = None
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Empty stack
        if self.first is None: 
            self.first = Node(x)
            self.last = Node(x)
            self.min = self.first
        else: 
            newNode = Node(x)
            # Update the minimum
            if x < self.min.val: 
                newNode.prevMin = self.min
                self.min = newNode
            # Update prev and next pointers
            newNode.prev = self.last
            self.last.next = newNode
            self.last = newNode
            

    def pop(self):
        """
        :rtype: None
        """
        if self.first is not None:
            # Update the minimum
            self.min = self.prevMin
            # Update pointers
            self.last = self.last.prev
            self.last.next = None


    def top(self):
        """
        :rtype: int
        """
        return self.last.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.min.val

        
class Node: 
    def __init__(self, val=None): 
        """
        A node in a single-linked list
        """
        self.val = val
        self.prev = None
        self.next = None
        self.prevMin = None
        
