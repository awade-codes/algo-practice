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
        # Example: [10, 20] -> enqueue(30) -> [10, 20, 30]
        self.items.append(item) 

    def dequeue(self):
        """ remove and return item from the front; return None if empty"""
        if self.is_empty():
            return None
        # Example: [10, 20, 30] -> dequeue() -> 10, list becomes [20, 30]
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

class Node: 
    """A node is a singley linked list"""
    def __init__(self,value): 
        self.value = value
        self.next = None    

class LinkedList: 
    """ a singlely linked list."""
    def __init__(self):
        self.head = None # points to the first node 

    def append(self,value):
        """ Create a new node"""
        new_node = Node(value)

        if self.head is None: 
            self.head = new_node
            return
        
        # walk to the end 
        current = self.head
        while current.next is not None: 
            current = current.next

        current.next = new_node

    def prepend(self, value):
        """Add a node with the given value to the front of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def find(self, value):
        """Return True if a node with the given value exists, else False."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def delete(self, value):
        """Delete the first node with the given value. Do nothing if not found."""
        if self.head is None:
            return

        # If the head node is to be deleted
        if self.head.value == value:
            self.head = self.head.next
            return

        prev = None
        current = self.head

        while current is not None:
            if current.value == value:
                # bypass current
                prev.next = current.next
                return
            prev = current
            current = current.next

    def to_list(self):
        """Return a Python list of all values in the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def length(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        


if __name__ == "__main__":
    # Simple manual tests for Stack class
    s = Stack()
    print("\nTesting Stack...")
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
    print("\nTesting Queue...")
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

    print("\nTesting LinkedList...")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)       # list: 5 -> 10 -> 20
    print(ll.to_list()) # [5, 10, 20]
    print(ll.find(10))  # True
    print(ll.find(99))  # False
    ll.delete(10)       # list: 5 -> 20
    print(ll.to_list()) # [5, 20]
    print(ll.length())  # 2
    ll.delete(5)        # list: 20
    print(ll.to_list()) # [20]
    ll.delete(20)       # list: empty
    print(ll.to_list()) # []
    print(ll.length())  # 0