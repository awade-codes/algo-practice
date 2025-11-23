# src/datastructures.py

class Stack:
    """A simple LIFO stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Return None if the stack is empty."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Return None if empty."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, else False."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

class Queue: 
    """ A simple FIFO queue implenation using a Python list"""
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """ Push an item to the back of the queue"""
        self.items.append(item)

    def dequeue(self):
        """ remove and return item from the front; return None if empty"""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """ return front item without removing; return None if empty"""
        if self.is_empty(): 
            return None
        return self.items[0]
    
    def is_empty(self):
        """ return True if empty"""
        return len(self.items) == 0
    
    def size(self): 
        """ return # of items"""
        return len(self.items)


    

if __name__ == "__main__":
    # Simple manual tests for Stack class
    s = Stack()
    print(s.is_empty())   # True
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())       # 30
    print(s.pop())        # 30
    print(s.pop())        # 20
    print(s.size())       # 1
    print(s.is_empty())   # False
    print(s.pop())        # 10
    print(s.pop())        # None
    print(s.is_empty())   # True

    # Tests for Queue class
    q = Queue()
    print(q.is_empty())   # True
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.peek())       # 10
    print(q.dequeue())    # 10
    print(q.dequeue())    # 20
    print(q.size())       # 1
    print(q.is_empty())   # False
    print(q.dequeue())    # 30
    print(q.dequeue())    # None
    print(q.is_empty())   # True