class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.entry = [0] * k
        self.length = k
        self.front = 0
        self.rear = -1
        self.counter = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.counter == self.length:
            return False
        else:
            self.rear = (self.rear + 1) % self.length 
            self.entry[self.rear] = value
            self.counter += 1
            return True
        


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.counter:
            self.front = (self.front+1) % self.length 
            self.counter -= 1
            return True
        else:
            return False
 
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.counter:
            return self.entry[self.front]
        else:
            return -1
        
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.counter: 
            return self.entry[self.rear]
        else:
            return -1
        
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.counter==0
 

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.counter == self.length