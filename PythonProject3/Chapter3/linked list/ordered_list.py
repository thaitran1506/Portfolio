"""
the structure of an ordered list is a collection of items where each item holds a relative
position that is based upon some underlying characteristic of the item. The ordering is
typically ascending or descending and we assume that list items have a meaningful comparison
operation that is already define.
- OrderedList() creates a new ordered list that is empty. It needs no parameters and returns an
empty list.
- add(item) adds a new item to the list making sure that the order is preserved. It needs the
item and returns nothing. Assume the item is not already in the list
- remove(item) remove the item from the list. Needs the item and modifies the list. It will
raise an error if item is not in the list
- search(item) searches for the item in the list. Needs the item and return a Boolean value
- is_empty() needs no parameters and returns a boolean value
- size() needs no parameters and return an integer
- index(item) return the position of an item in the list, assuming the item is in the list
- pop() removes and returns the last item in the list
- pop(pos) removes and returns the item at the position pos. It needs the position and returns
the item. Assume the item is in the list
"""
import node

"""to implement the ordered list, we will use the same technique as seen previously with unordered
list. It's an empty list with head reference to None"""
class OrderedList:
    """create an empty ordered list with head refers to None"""
    def __init__(self):
        self.head = None

    """the is_empty and size methods can be implemented the same as with unordered list as they 
    deal only with the number of nodes in the list without regard to the actual item values. The remove 
    method will also work just fine"""

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next

        return count

    def remove(self, item):
        current = self.head
        previous = None

        while current.next is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("The item is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    """The search of an unordered linked list required that we traverse the nodes one at a time 
    until we either find the item we are looking for or run out of nodes (None). However, in the
    case where the item is not in the list, we can take advantage of the ordering to stop the search
    as soon as current.data is greater than item."""
    def search(self):
