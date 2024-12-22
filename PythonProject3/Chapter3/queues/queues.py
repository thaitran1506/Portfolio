"""
A queue is an ordered collection of items where the addition of new items happens at one end, called the rear, and
the removal of existing items occurs at the other end, commonly called the front. As an element enters the queue, it
starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.
The most recently added item in the queue must wait at the end of the collection. The item that has been in the collection
the longest is at the front. This ordering principle is called FIFO, first-in-first-out (FIFO) or first come, first served.
The queue ADT is defined as follows:
Queue() create a new queue that is empty. It needs no parameters and return and empty queue
enqueue(item) adds a new item to the end of the queue. It needs the item and returns nothing.
dequeue() removes the item at the front of the queue. It needs no parameters. It returns nothing.
is_empty() returns True if the queue is empty, False otherwise. Needs no parameters.
size() returns the number of items in the queue. Needs no parameters.
"""
class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item): #enqueue will be O(n)
        self._items.insert(0, item)

    def dequeue(self): #dequeue will be O(1)
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

