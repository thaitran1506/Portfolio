"""
The unordered linked list will be built from a collection of nodes, each linked to the next by
explicit references. As long as we know where to find the first node, each item after that can
be found by successively following the next links.
The UnorderedList class must maintain a reference to the first node.
"""
import node

class UnorderedList:
    def __init__(self):
        self.head = None #initially when we construct a list, there is no item. And the head of the list
        #points to None

    """the is_empty method checks to see if the linked list is empty. If the head of the list points 
    to None, then the list is empty."""
    def is_empty(self):
        return self.head is None

    """we also need to be able to add item to the list. 
    the add method is shown below. Each item of the list must reside the node object. 
    Link the new node into the existing structure. This requires 2 steps:
    1. change the next reference of the new node to refer to the old first node of the list.
    2. Modify the head of the list to refer to the new node. 
    """
    def add(self, item):
        temp = node.Node(item)
        temp.set_next(self.head)
        self.head = temp

    """The next methods size, search, and remove are all based on a technique known as linked 
    list traversal. Traversal refers to the process of systematically visiting each node. To do this
    we use an external reference that starts at the first node in the list. As we visit each node, 
    we move the reference to the next node by traversing the next reference.
    To implement the size method, we need to traverse the linked list and keep a count of the number 
    of nodes that occurred. The external reference is called current and is initialized to the head 
    of the list. At the start of the process, the count is set to 0. As long as the current reference
    has not seen the end of the list (None), we move current along to the next node. Everytime 
    current moves to a new node, we add 1 to count. Finally count gets returned after the iteration stops."""

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    """searching for a value in linked list also uses the traversal technique. As we visit each node in
    the linked list we will ask whether the data stored there matches the item we are look for. 
    We do not have to traverse all the way to end of the list. If we do get to the end of the list, 
    that means the item we are looking for must not be present. Also, if we find it, no need to continue
    """
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    """The remove method requires two logical steps. First we need to traverse the list looking for
    the item we want to remove. Once we find the item, we must remove it. If the item is not in the list
    , our method should raise a ValueError.
    We will use two external references as we traverse down the linked list. Current will behave just
    as it did before, marking the location of the traversal. The new reference, which we call previous
    will always travel one node behind current. When current stops at the node to be removed, previous
    will refer to the proper place in the linked list. 
    Note that current starts out at the list head, previous, however is assumed to always travel
    one node behind current. For this reason, previous starts out with a value of None, since there is
    no node before the head. 
    """
    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if current is None:
            """special case where item is not in the list, current traverses to the end of the list."""
            raise ValueError("The item you are looking for is not in the list")
        if previous is None:
            """special case where the item to be removed is the head of the list (current is head, previous is None). Then point the
            head of the list to the next node after the current node."""
            self.head = current.next
        else:
            previous.next = current.next
