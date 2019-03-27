class MinStack(object):

    def __init__(self):
        """
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
        newNode = Node(x)
        # Empty stack
        if self.first is None: 
            self.first = newNode
            self.last = newNode
            self.min = self.first
        else: 
            # Update the minimum
            if x < self.min.val: 
                newNode.prevMin = self.min
                self.min = newNode
            else: 
                newNode.prevMin = self.min
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
            self.min = self.last.prevMin
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
        if self is not None: 
            return self.min.val

        
class Node: 
    def __init__(self, val=None): 
        """
        A node in a double-linked list
        """
        self.val = val
        self.prev = None
        self.next = None
        self.prevMin = None


def tests(): 
    s = MinStack()
    s.push(1)
    s.push(-1)
    s.push(0)
    print(s.first.val == 1)
    print(s.last.val == 0)
        
    s.pop()
    print(s.top() == -1)
    print(s.getMin() == -1)
    s.pop()
    print(s.getMin() == 1)
    s.pop()
    s.top()

tests()
