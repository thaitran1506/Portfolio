"""
The deque ADT is defined by the following structure and operations. A deque is structured, as described above, as an
ordered collection of items where items are added and removed from either end, either front or rear. The deque operations
are give below:
- Deque() creates a new deque that is empty. No need parameters and return nothing
- add_front(item) adds a new item to the front. Needs the item and returns nothing
- add_rear(item) adds a new item to the rear. Needs the item and returns nothing
- remove_front() remove item at the front. Needs no parameters and return the item. Deque is modified
- remove_rear() remove item at the rear. Needs no parameters and return the item. Deque is modified
- is_empty() needs no parameters and returns True is deque is empty
- size() returns the number of items in deque
"""

class Deque:
    """
    Represents a double-ended queue (deque) data structure.

    A Deque allows adding and removing elements from both ends. Provides
    methods to perform these operations as well as to check its current
    status or size. This implementation uses an underlying Python list
    to maintain elements.

    :ivar items: Internal list storing the elements of the deque.
    :type items: list
    """
    #create an empty deque
    def __init__(self):
        self.items = []

    #add new item to front of the deque
    def add_front(self, item):
        self.items.append(item)
    #add new item to the rear of the deque
    def add_rear(self, item):
        self.items.insert(0,item)
    #remove item in the front
    def remove_front(self):
        return self.items.pop()
    #remove item in the rear
    def remove_rear(self):
        return self.items.pop(0)
    #check to see if a deque is empty
    def is_empty(self):
        return not bool(self.items)
    #return the size of the deque
    def size(self):
        return len(self.items)



